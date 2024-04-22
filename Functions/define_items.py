class Upgrade():
  def __init__(self, type, cost, description, value, icon):
    self.type = type
    self.cost = cost
    self.description = description
    self.value = value
    self.icon = icon



class Powerup():
  def __init__(self, type, cost, description, icon):
    self.type = type
    self.cost = cost
    self.description = description
    self.icon = icon



class Active_Powerups():
  def __init__(self, energy, double, teleport, score, nerd, nerdd):
    self.energy = energy
    self.double = double
    self.teleport = teleport
    self.score = score
    self.nerd = nerd#add new
    self.nerdd = nerdd#add new

  def purchase(self, type):
    if type == 'Energy Drink':
      self.energy += 100
    elif type == 'Double Sisyphus':
      self.double += 10
    elif type == 'Teleport':
      self.teleport = -1
    elif type == 'Score Booster':
      self.score += 250
    elif type == 'nerd':
      self.nerd += 10
    elif type == 'nerdd':
      self.nerdd += 10
  
  def decrease_duration(self):
    if self.energy > 0:
      self.energy -= 1
    elif self.double > 0:
      self.double -= 1
    elif self.teleport > 0:
      self.teleport -= 1
    elif self.score > 0:
      self.score -= 1
    elif self.nerd > 0:
      self.nerd -= 1
    elif self.nerdd > 0:
      self.nerdd -= 1
  
  def change_prices(self, right_platform_value):
    self.teleport = right_platform_value


def define_upgrades():
  upgrades = []

  strength = []
  type = 'Strength'
  description = (
    'Strength Training:',
    'Increases the player\'s overall strength,',
    'allowing them to push the boulder faster.'
  )
  icon = 'Sprites/Items/Bicep.png'
  strength.append(Upgrade(
    type, 0, description+('$50','1.0 -> 1.5 per tick'), 1.0, icon
  ))
  strength.append(Upgrade(
    type, 50, description+('$250','1.5 -> 2.0 per tick'), 1.5, icon
  ))
  strength.append(Upgrade(
    type, 250, description+('MAX TIER',), 2.0, icon
  ))
  upgrades.append(strength)

  endurance = []
  type = 'Endurance'
  description = (
    'Endurance Training:',
    'Improves the player\'s endurance,',
    'reducing the rate at which exhaustion builds up.'
  )
  icon = 'Sprites/Items/Value.png'
  endurance.append(Upgrade(
    type, 0, description+('$100','2.5 -> 2.0 per tick'), 2.5, icon
  ))
  endurance.append(Upgrade(
    type, 100, description+('$500','2.0 -> 1.5 per tick'), 2.0, icon
  ))
  endurance.append(Upgrade(
    type, 500, description+('MAX TIER',), 1.5, icon
  ))
  upgrades.append(endurance)
  
  stamina = []
  type = 'Stamina'
  description = (
    'Stamina Training:',
    'Enhances the player\'s stamina, increasing the rate at which exhaustion decreases.'
  )
  icon = 'Sprites/Items/Value.png'
  stamina.append(Upgrade(
    type, 0, description+('$50','1.0 -> 2.0 per tick'), 1.0, icon
  ))
  stamina.append(Upgrade(
    type, 50, description+('$100','2.0 -> 2.5 per tick'), 2.0, icon
  ))
  stamina.append(Upgrade(
    type, 100, description+('MAX TIER',), 2.5, icon
  ))
  upgrades.append(stamina)

  value = []
  type = 'Value'
  description = (
    'Boulder Value Increase:',
    'Increases the value of the boulder,',
    'resulting in greater profits when reaching hills.'
  )
  icon = 'Sprites/Items/Value.png'
  value.append(Upgrade(
    type, 0, description+('$100','1.0x -> 1.5x'), 1.0, icon
  ))
  value.append(Upgrade(
    type, 100, description+('$500','1.5x -> 2.0x'), 1.5, icon
  ))
  value.append(Upgrade(
    type, 500, description+('$1000','2.0x -> 2.5x'), 2.0, icon
  ))
  value.append(Upgrade(
    type, 1000, description+('MAX TIER',), 2.5, icon
  ))
  upgrades.append(value)

  maximum = []
  type = 'Longer Hill'
  description = (
    'Longer Hill:',
    'Clears out the path to allow the boulder to be pushed further.'
  )
  icon = 'Sprites/Items/Value.png'
  maximum.append(Upgrade(
    type, 0, description+('$50','2 -> 3'), 2, icon
  ))
  maximum.append(Upgrade(
    type, 50, description+('$100','3 -> 4'), 3, icon
  ))
  maximum.append(Upgrade(
    type, 100, description+('$500','4 -> 5'), 4, icon
  ))
  maximum.append(Upgrade(
    type, 500, description+('$1000','5 -> 6'), 5, icon
  ))
  maximum.append(Upgrade(
    type, 1000, description+('MAX TIER',), 6, icon
  ))
  upgrades.append(maximum)

  music = []
  type = 'Music'
  description = (
    'Extra Music:',
    'Adds another song to the background audio.'
  )
  icon = 'Sprites/Items/Music Note.png'
  music.append(Upgrade(
    type, 0, description+('$100','a song (probably)'), 1, icon
  ))
  music.append(Upgrade(
    type, 100, description+('MAX TIER',), 2, icon
  ))
  upgrades.append(music)
  
  return(upgrades)



def define_powerups():
  powerups = []

  powerups.append(Powerup(
    'Energy Drink',
    10,
    (
      'Energy Drink:',
      'Provides a boost of energy that increases speed',
      'at the cost of endurance for a short duration.',
      'Lasts 100 ticks.'
    ),
    'Sprites/Items/Energy Drink.png'
  ))

  powerups.append(Powerup(
    'Double Sisyphus',
    10,
    (
      'Double Sisyphus:',
      'Summons a second Sisyphus that automatically',
      'rolls his boulder up the hill.',
      'doesnt do anything yet, feel free to waste money'
    ),
    'Sprites/Items/Value.png'
  ))
  
  powerups.append(Powerup(
    'Teleport',
    10,
    (
      'Teleport:',
      'Allows the player to instantly teleport',
      'to a higher section of the hill, skipping',
      'a portion of the uphill journey.',
      'Immediate.'
    ),
    'Sprites/Items/Portals.png'
  ))

  powerups.append(Powerup(
    'Score Booster',
    10,
    (
      'Score Booster:',
      'Temporarily doubles the value of each hill.',
      'Lasts 250 ticks.'
    ),
    'Sprites/Items/Value.png'
  ))

  powerups.append(Powerup(
    'nerd',
    1000,
    (
      'nerd:',
      'i havent decided on what to add here',
      '$1000',
      'doesnt do anything yet, feel free to waste money'
    ),
    'Sprites/Items/Value.png'
  ))

  powerups.append(Powerup(
    'nerdd',
    1000,
    (
      'nerdd:',
      'i havent decided on what to add here',
      '$1000',
      'doesnt do anything yet, feel free to waste money'
    ),
    'Sprites/Items/Value.png'
  ))
  
  return(powerups)



def define_active():
  active_powerups = Active_Powerups(0, 0, 0, 0, 0, 0)
  return(active_powerups)
