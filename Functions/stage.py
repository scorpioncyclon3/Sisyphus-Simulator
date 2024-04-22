from Functions.make_hill import make_hill
from Functions.render_text import render_text

# thanks Rabbid76 from StackOverflow
def blitRotateCenter(pygame, surf, image, topleft, angle):
  rotated_image = pygame.transform.rotate(image, angle)
  new_rect = rotated_image.get_rect(center = image.get_rect(topleft = topleft).center)
  surf.blit(rotated_image, new_rect)

def stage(
  pygame, screen, boulder, boulder_type,
  platforms, max_platform, left_platform,
  active_powerups, score, exhaustion
):
  # makes the stage
  screen.fill((105, 69, 38))

  # info
  comicsans = pygame.font.SysFont(None, 25)
  label = comicsans.render(f'Score - {int(score)}', 1, (255, 255, 255))
  screen.blit(label, (250, 10))
  label = comicsans.render(f'Exhaustion - {int(exhaustion)}%', 1, (255, 255, 255))
  screen.blit(label, (250, 35))

  # renders the boulder
  boulder_types = {
    1.0 : 'Sprites/Boulders/Boulder.png',
    1.5 : 'Sprites/Boulders/Gilded Boulder.png',
    2.0 : 'Sprites/Boulders/Golden Boulder.png',
    2.5 : 'Sprites/Boulders/Golden Boulder.png'
  }
  boulder_img = pygame.image.load(boulder_types[boulder_type])
  blitRotateCenter(pygame, screen, boulder_img,
    (boulder.x - boulder.size, boulder.y - boulder.size),
    boulder.rotation)

  # portal
  if active_powerups.teleport > 0:
    pygame.draw.rect(screen, (105, 69, 38), (250, 250, 50, 50))
    rect = pygame.Rect(
      platforms[left_platform].find_left()[0], platforms[left_platform].y - 25, 5, 25
    )
    pygame.draw.rect(screen, (50, 150, 255), rect)
  
  # creates hills
  make_hill(pygame, screen, platforms, max_platform)

  # shop
  rect = pygame.Rect(25, 25, 100, 50)
  pygame.draw.rect(screen, (150, 150, 150), rect)
  pygame.draw.rect(screen, (0, 0, 0), rect, 5)
  comicsans = pygame.font.Font('COMIC.ttf', 30)
  render_text(screen, comicsans, 75, 50, (0, 0, 0), 255, 'SHOP')
