from Functions.render_text import render_text

def create_item(pygame, screen, x, y, item):
  rect = pygame.Rect(x - 40, y - 25, 80, 50)
  if item.description[-1] == 'MAX TIER':
    pygame.draw.rect(screen, (191, 184, 126), rect)
  else:
    pygame.draw.rect(screen, (150, 150, 150), rect)
  pygame.draw.rect(screen, (50, 50, 50), rect, 5)
  # loads the icon
  icon = pygame.image.load(item.icon)
  screen.blit(icon, (x - 10, y - 15))
  # adds a caption
  comicsans = pygame.font.Font("COMIC.ttf", 10)
  render_text(screen, comicsans, x, y + 10, (0, 0, 0), 255, item.type)



def item_interactions(pygame, screen, x, y, score, mouse_pos, clicked, item):
  purchased = False
  comicsans = pygame.font.Font("COMIC.ttf", 10)
  # if the cursor is hovering over the item, creates an item description
  if (x - 40) < mouse_pos[0] < (x + 40) and (y - 25) < mouse_pos[1] < (y + 25):
    # calculates the dimensions of the largest block of text
    text_width = 0
    text_height = 0
    for line in item.description:
      if comicsans.size(line)[0] > text_width:
        text_width = comicsans.size(line)[0]
      if comicsans.size(line)[1] > text_height:
        text_height = comicsans.size(line)[1]
    # creates a text box
    rect = pygame.Rect(
      int(mouse_pos[0] - text_width) - 5,
      int(mouse_pos[1] - 
        (text_height * len(item.description) / 2)) - 5,
      text_width + 10,
      text_height * len(item.description) + 10)
    pygame.draw.rect(screen, (255, 255, 255), rect)
    pygame.draw.rect(screen, (0, 0, 0), rect, 2)

    # adds each line to the description
    for i in range(len(item.description)):
      # prepares text
      label = comicsans.render(item.description[i], 1, (0,  0,0))
      # positions the text and renders
      screen.blit(label, (
        int(mouse_pos[0] - text_width), 
        int(mouse_pos[1] - (text_height * 
           (len(item.description) - i - 
           (len(item.description) / 2)))
        ))
      )
    
    # if the player clicked on the upgrade
    if clicked:
      purchased = True
  
  return(score, item, purchased)



def shop(pygame, screen, score, clicked, upgrades, powerups, active_powerups):
  mouse_pos = pygame.mouse.get_pos()
  
  # makes the stage
  screen.fill((100, 100, 100))

  # info
  comicsans = pygame.font.Font("COMIC.ttf", 10)
  label = comicsans.render(f"Score - {int(score)}", 1, (255, 255, 255))
  screen.blit(label, (10, 10))

  # left
  rect = pygame.Rect(0, 0, 200, 350)
  pygame.draw.rect(screen, (50, 50, 50), rect, 5)
  # exit
  rect = pygame.Rect(50, 250, 100, 50)
  pygame.draw.rect(screen, (150, 150, 150), rect)
  pygame.draw.rect(screen, (50, 50, 50), rect, 5)
  comicsans = pygame.font.Font("COMIC.ttf", 30)
  render_text(screen, comicsans, 100, 275, (0, 0, 0), 255, 'EXIT')
  if 50 < mouse_pos[0] < 150 and 250 < mouse_pos[1] < 300 and clicked:
    shop_open = False
  else:
    shop_open = True
  # saving
  rect = pygame.Rect(50, 175, 100, 50)
  pygame.draw.rect(screen, (150, 150, 150), rect)
  pygame.draw.rect(screen, (50, 50, 50), rect, 5)
  comicsans = pygame.font.Font("COMIC.ttf", 30)
  render_text(screen, comicsans, 100, 200, (0, 0, 0), 255, 'SAVE')
  if 50 < mouse_pos[0] < 150 and 175 < mouse_pos[1] < 225 and clicked:
    save_menu_open = True
    shop_open = False
  else:
    save_menu_open = False
  
  # top right
  rect = pygame.Rect(200, 0, 300, 175)
  pygame.draw.rect(screen, (50, 50, 50), rect, 5)
  # title
  rect = pygame.Rect(275, 0, 150, 50)
  pygame.draw.rect(screen, (150, 150, 150), rect)
  pygame.draw.rect(screen, (50, 50, 50), rect, 5)
  comicsans = pygame.font.Font("COMIC.ttf", 25)
  render_text(screen, comicsans, 350, 25, (0, 0, 0), 255, 'Upgrades')
  counter = 0
  for y in range(80, 141, 60):
    for x in range(260, 441, 90):
      create_item(
        pygame, screen, x, y, upgrades[counter][0]
      )
      counter += 1
  
  # bottom right
  rect = pygame.Rect(200, 175, 300, 175)
  pygame.draw.rect(screen, (50, 50, 50), rect, 5)
  # title
  rect = pygame.Rect(275, 175, 150, 50)
  pygame.draw.rect(screen, (150, 150, 150), rect)
  pygame.draw.rect(screen, (50, 50, 50), rect, 5)
  comicsans = pygame.font.Font("COMIC.ttf", 25)
  render_text(screen, comicsans, 350, 200, (0, 0, 0), 255, 'Powerups')
  counter = 0
  for y in range(255, 316, 60):
    for x in range(260, 441, 90):
      create_item(
        pygame, screen, x, y, powerups[counter]
      )
      counter += 1
  
  # item interactions
  counter = 0
  for y in range(80, 141, 60):
    for x in range(260, 441, 90):
      item = upgrades[counter][0]
      score, upgrades[counter][0], purchased = item_interactions(
        pygame, screen, x, y, score, mouse_pos, clicked, item
      )
      # if the player tried to purchase the upgrade
      if purchased:
        # if the upgrade is not maxed out and the player can afford it
        if item.description[-1] != 'MAX TIER' and score >= item.cost:
          # removes the current tier
          upgrades[counter] = upgrades[counter][1:]
          # subtracts the cost of the upgrade
          score -= item.cost
      # goes to the next item
      counter += 1
  
  counter = 0
  for y in range(255, 316, 60):
    for x in range(260, 441, 90):
      item = powerups[counter]
      score, powerups[counter], purchased = item_interactions(
        pygame, screen, x, y, score, mouse_pos, clicked, item
      )
      if purchased:
        # if the player can afford it
        if score >= item.cost:
          active_powerups.purchase(item.type)
          # subtracts the cost of the upgrade
          score -= item.cost
      # goes to the next item
      counter += 1
  
  return(shop_open, save_menu_open, score, upgrades, powerups, active_powerups)
