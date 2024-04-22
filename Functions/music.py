def music(pygame, songs):
  """if not pygame.mixer.music.get_busy():
    for song in songs:
      pygame.mixer.music.queue(f'Music/{song}')
  pygame.mixer.music.play()
  print(pygame.mixer.music.get_busy())"""
  pygame.mixer.init()
  try:
    pygame.mixer.init()
    #pygame.mixer.init(devicename=None)
    #pygame.mixer.init(devicename=None, frequency=44100, size=-16, channels=2, buffer=4096)
    #pygame.mixer.init(devicename='Dummy')
    print('music initialised')
  except pygame.error:
    try:
      #pygame.mixer.music.load(f'Music/{songs[0]}')
      pygame.mixer.music.load(songs[0])
      print('loaded')
      pygame.mixer.music.play()
      print(songs[0])
    except pygame.error:
      pass
    except:
      print('different error???')
  except:
    print('different error???')
