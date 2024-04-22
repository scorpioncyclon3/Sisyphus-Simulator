import pygame
from random import randint
from Functions.render_text import render_text
from Functions.stage import stage
from Functions.shop import shop
from Functions.define_items import define_upgrades
from Functions.define_items import define_powerups
from Functions.define_items import define_active
from Functions.save import save
from Functions.music import music

class Platform:
  def __init__(self, x, y, value):
    self.x = x
    self.y = y
    self.value = value
  
  def find_left(self):
    return((self.x - 15, self.y))

  def find_right(self):
    return((self.x + 15, self.y))

class Boulder:
  def __init__(
    # current position and movement
    self, x, y, size, rotation, falling, pushing,
    # platforms
    platforms, left_platform, right_platform
  ):
    # position
    self.x = x
    self.y = y
    # radius
    self.size = size
    # degrees
    self.rotation = rotation
    # booleans
    self.falling = falling
    self.pushing = pushing
    # the platform on either side
    self.left_platform = left_platform
    self.right_platform = right_platform

  def find_pos(self):
    return((self.x, self.y))

  def position_y(self):
    # if the player is on a platform
    if self.x < platforms[self.left_platform].find_right()[0]:
      y = platforms[self.left_platform].y
    elif self.x > platforms[self.right_platform].find_left()[0]:
      y = platforms[self.right_platform].y

    # if the player is between platforms
    else:
      # finds the gradient of the hill
      run = (
        (platforms[self.right_platform].find_left()[0]) - 
        (platforms[self.left_platform].find_right()[0])
      )
      rise = (
        platforms[self.left_platform].y - 
        platforms[self.right_platform].y
      )
      gradient = rise / run
      # positions on the hill
      distance_from_left = self.x - (platforms[self.left_platform].find_right()[0])
      y = platforms[self.left_platform].y - gradient * distance_from_left
      
      # if the player is resting on a hill, start falling
      if not self.pushing and not self.falling:
        self.falling = True
        print('stopped on hill')

    # returns the calculated position
    return(y - self.size)



# defines the position and value of each platform
platforms = [
  Platform(50, 300, 0),
  Platform(100, 290, 10),
  Platform(155, 275, 25),
  Platform(215, 250, 50),
  Platform(275, 225, 100),
  Platform(345, 190, 250),
  Platform(425, 140, 500),
  Platform(500, 75, 1000),
]

# defines the boulder
boulder = Boulder(50.0, 50.0, 10, 0, False, False, platforms, 0, 1)
boulder.y = boulder.position_y()

upgrades = define_upgrades()
powerups = define_powerups()
active_powerups = define_active()

score = 23786540.0
exhaustion = 0.0
max_platform = 2
player_speed = 1.0
exhaustion_rate = 2.5
recovery_rate = 1.0
score_multiplier = 1.0
clicked = False
mouse_pos = (0, 0)
shop_open = False
save_menu_open = False
username = ''
songs = ['Me and the Birds.mp3']



pygame.init()
#pygame.mixer.init(devicename='dummy')
screen = pygame.display.set_mode((500, 350))
pygame.display.set_caption('pygam')
clock = pygame.time.Clock()

running = True

while running:
  clock.tick(30)
  clicked = False

  events = pygame.event.get()
  # interactions
  for event in events:
    # exit
    if event.type == pygame.QUIT:
      running = False
    # clicks
    if event.type == pygame.MOUSEBUTTONDOWN:
      mouse_pos = pygame.mouse.get_pos()

      clicked = True
      print('Clicked at', mouse_pos)

  if shop_open:
    shop_open, save_menu_open, score, upgrades, powerups, active_powerups = shop(
      pygame, screen, score, clicked, upgrades, powerups, active_powerups
    )

    # changes upgrades
    player_speed = upgrades[0][0].value
    exhaustion_rate = upgrades[1][0].value
    recovery_rate = upgrades[2][0].value
    score_multiplier = upgrades[3][0].value
    max_platform = upgrades[4][0].value

    # changes powerup costs
    powerups[2].cost = (platforms[boulder.right_platform]).value
    if boulder.right_platform == max_platform:
      powerups[2].cost = score + 1
    
    # if the player purchased the teleport powerups
    if active_powerups.teleport < 0:
      boulder.x = platforms[boulder.right_platform].x
      boulder.y = boulder.position_y()
      boulder.left_platform += 1
      boulder.right_platform += 1
      active_powerups.teleport = 10
    
  
  elif save_menu_open:
    save_menu_open, username, score, upgrades, powerups, active_powerups = save(
      pygame, screen, events, username, score, upgrades, powerups, active_powerups
    )
    if not save_menu_open:
      player_speed = upgrades[0][0].value
      exhaustion_rate = upgrades[1][0].value
      recovery_rate = upgrades[2][0].value
      score_multiplier = upgrades[3][0].value
      max_platform = upgrades[4][0].value
      boulder.x = 50.0
      boulder.y = boulder.position_y()
      boulder.rotation = 0
      boulder.falling = False
      boulder.pushing = False
      boulder.left_platform = 0
      boulder.right_platform = 1
    
    
  else:
    pressed = pygame.key.get_pressed()
    # player is pushing the boulder
    if pressed[pygame.K_SPACE] and not boulder.falling:
      # moves the boulder
      # if the player has drinken an energy drink
      if active_powerups.energy > 0:
        boulder.x += player_speed * 0.5
        boulder.rotation -= int(player_speed * 2.5)
        exhaustion += exhaustion_rate * 0.5
      boulder.pushing = True
      boulder.x += player_speed
      boulder.y = boulder.position_y()
      boulder.rotation -= int(player_speed * 5)
      boulder.rotation = boulder.rotation % 360
      # increases exhaustion
      exhaustion += exhaustion_rate
      if exhaustion >= 100.0:
        boulder.falling = True
        exhaustion = 100.0
        print('exhausted')
  
      # if the boulder approaches a new hill
      if boulder.x > platforms[boulder.right_platform].x and not boulder.falling:
        # increases score
        score += platforms[boulder.right_platform].value * score_multiplier
        # if double score is active
        if active_powerups.score > 0:
          score += platforms[boulder.right_platform].value * score_multiplier
        print(score)
        # raises the left and right platform tracking
        boulder.left_platform += 1
        boulder.right_platform += 1
        # if the boulder is at the highest available platform
        if boulder.left_platform == max_platform:
          boulder.falling = True
          print('too high')
    
    # if not pushing
    else:
      boulder.pushing = False
      boulder.y = boulder.position_y()
      # decreases exhaustion if resting
      exhaustion -= recovery_rate
      if exhaustion <= 0:
        exhaustion = 0
    
    if boulder.falling:
      boulder.x -= 5.0
      boulder.y = boulder.position_y()
      boulder.rotation += 25
      boulder.rotation = boulder.rotation % 360
      # if the boulder is at the bottom
      if boulder.x < platforms[0].x:
        boulder.falling = False
        boulder.x = platforms[0].x
        exhaustion = 0.0
      # if the boulder approaches a new hill
      elif boulder.x < platforms[boulder.left_platform].x:
        boulder.left_platform -= 1
        boulder.right_platform -= 1
  
  
  
    # makes the stage
    stage(
      pygame, screen, boulder, score_multiplier,
      platforms, max_platform, boulder.left_platform,
      active_powerups, score, exhaustion
    )
    #pygame.mixer.music.load(songs[0])
    #pygame.mixer.music.play()
    music(pygame, songs)



    if clicked:
      if 25 < mouse_pos[0] < 125 and 25 < mouse_pos[1] < 75:
        shop_open = True
      mouse_pos = (0, 0)
    
    active_powerups.decrease_duration()
  # saves changes to the screen
  pygame.display.update()
# closes pygame
pygame.display.quit()
