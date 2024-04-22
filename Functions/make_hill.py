def make_hill(pygame, screen, platforms, max_platform):
  # fills in hill
  # left of hill
  pygame.draw.polygon(screen, (107, 50, 20), (
    (0,250),
    platforms[0].find_left(),
    (platforms[0].find_left()[0], 350),
    (0, 350)))
  for i in range(len(platforms)-1):
    # below each platform
    pygame.draw.polygon(screen, (107, 50, 20), (
      platforms[i].find_left(),
      platforms[i].find_right(),
      (platforms[i].find_right()[0], 350),
      (platforms[i].find_left()[0], 350)))
    # between platforms
    pygame.draw.polygon(screen, (107, 50, 20), (
      platforms[i].find_right(),
      platforms[i+1].find_left(),
      (platforms[i+1].find_left()[0], 350),
      (platforms[i].find_right()[0], 350)))
  # below final platform
  pygame.draw.polygon(screen, (107, 50, 20), (
    platforms[-1].find_left(),
    platforms[-1].find_right(),
    (platforms[-1].find_right()[0], 350),
    (platforms[-1].find_left()[0], 350)))
  
  # outline
  # left of the hill
  pygame.draw.line(
    screen, (0, 0, 0), (0, 250), platforms[0].find_left(), width=5
  )
  for i in range(len(platforms)-1):
    # platform
    pygame.draw.line(
      screen, (0, 0, 0), platforms[i].find_left(), platforms[i].find_right(), width=5
    )
    # between platforms
    pygame.draw.line(
      screen, (0, 0, 0), platforms[i].find_right(), platforms[i+1].find_left(), width=5
    )
    if i >= max_platform:
      rect = pygame.Rect(
        platforms[i].find_right()[0], platforms[i].y - 25, 5, 25
      )
      pygame.draw.rect(screen, (50, 50, 50), rect)
  # final platform
  pygame.draw.line(
    screen, (0, 0, 0), platforms[-1].find_left(), platforms[-1].find_right(), width=5
  )
