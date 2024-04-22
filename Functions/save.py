from Functions.render_text import render_text
from Functions.define_items import define_upgrades
from Functions.define_items import define_powerups
from Functions.define_items import define_active
from replit import db

def save(pygame, screen, events, username, score, upgrades, powerups, active_powerups):
  mouse_pos = pygame.mouse.get_pos()
  clicked = False
  for event in events:
    # clicks
    if event.type == pygame.MOUSEBUTTONDOWN:
      clicked = True
    if event.type == pygame.KEYDOWN:
      keys = [
        'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
        'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',
      ]
      if event.key == pygame.K_BACKSPACE:
        username = username[0 : -1]
      elif pygame.key.name(event.key).upper() in keys:
        username += pygame.key.name(event.key).upper()

  # makes the stage
  screen.fill((100, 100, 100))
  rect = pygame.Rect(0, 0, 500, 350)
  pygame.draw.rect(screen, (50, 50, 50), rect, 5)
  comicsans = pygame.font.Font("COMIC.ttf", 30)
  render_text(screen, comicsans, 250, 50, (0, 0, 0), 255, 'type something')
  render_text(screen, comicsans, 250, 100, (0, 0, 0), 255, username)
  # for later use
  comicsans = pygame.font.Font("COMIC.ttf", 30)
  
  # exit
  rect = pygame.Rect(50, 250, 100, 50)
  pygame.draw.rect(screen, (150, 150, 150), rect)
  pygame.draw.rect(screen, (50, 50, 50), rect, 5)
  render_text(screen, comicsans, 100, 275, (0, 0, 0), 255, 'EXIT')
  if 50 < mouse_pos[0] < 150 and 250 < mouse_pos[1] < 300 and clicked:
    save_menu_open = False
  else:
    save_menu_open = True
  
  # load
  rect = pygame.Rect(200, 250, 100, 50)
  pygame.draw.rect(screen, (150, 150, 150), rect)
  pygame.draw.rect(screen, (50, 50, 50), rect, 5)
  render_text(screen, comicsans, 250, 275, (0, 0, 0), 255, 'LOAD')
  if 200 < mouse_pos[0] < 300 and 250 < mouse_pos[1] < 300 and clicked:
    if username in db.keys():
      # decompresses the users save into variables
      user_data = db[username].split()
      print(user_data)
      # score
      score = float(user_data[0].split(':')[1])
      score = 1000000000.0

      #upgrades
      upgrades = define_upgrades()
      
      # strength
      upgrade_count = int(user_data[1].split(':')[1])
      # removes out any previous upgrade tiers
      upgrades[0] = upgrades[0][upgrade_count:]
      
      # endurance
      upgrade_count = int(user_data[2].split(':')[1])
      # removes out any previous upgrade tiers
      upgrades[1] = upgrades[1][upgrade_count:]
      
      # stamina
      upgrade_count = int(user_data[3].split(':')[1])
      # removes out any previous upgrade tiers
      upgrades[2] = upgrades[2][upgrade_count:]
      
      # value
      upgrade_count = int(user_data[4].split(':')[1])
      # removes out any previous upgrade tiers
      upgrades[3] = upgrades[3][upgrade_count:]
      
      # max platform
      upgrade_count = int(user_data[5].split(':')[1])
      # removes out any previous upgrade tiers
      upgrades[4] = upgrades[4][upgrade_count:]
      
      # music
      upgrade_count = int(user_data[6].split(':')[1])
      # removes out any previous upgrade tiers
      upgrades[5] = upgrades[5][upgrade_count:]

      # resets powerups
      powerups = define_powerups()
      active_powerups = define_active()
  
  # save
  rect = pygame.Rect(350, 250, 100, 50)
  pygame.draw.rect(screen, (150, 150, 150), rect)
  pygame.draw.rect(screen, (50, 50, 50), rect, 5)
  render_text(screen, comicsans, 400, 275, (0, 0, 0), 255, 'SAVE')
  if 350 < mouse_pos[0] < 450 and 250 < mouse_pos[1] < 300 and clicked:
    # compresses the users save into a single string
    default = define_upgrades()
    if username:
      db[username] = (
        f'score:{score} '
        f'strength:{len(default[0]) - len(upgrades[0])} '
        f'endurance:{len(default[1]) - len(upgrades[1])} '
        f'stamina:{len(default[2]) - len(upgrades[2])} '
        f'value:{len(default[3]) - len(upgrades[3])} '
        f'hill_len:{len(default[4]) - len(upgrades[4])} '
        f'music:{len(default[5]) - len(upgrades[5])}'
      )
    else:
      db[username] = (
        'score:0.0 '
        'strength:0 '
        'endurance:0 '
        'stamina:0 '
        'value:0 '
        'hill_len:0 '
        'music:0'
      )
  return(save_menu_open, username, score, upgrades, powerups, active_powerups)
