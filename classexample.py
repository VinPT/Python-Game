class Room:
  """Making a room class for the game. Rooms has a width and height, doors, enemies, and chests.
  These will all be other classes. """    
    
  def __init__(self, width, height, doors, enemies, chests, character):
    self.width = width
    self.height = height
    self.doors = doors
    self.enemies = enemies
    self.chests = chests
    self.character = character


class Character:
  def position(self):
    self.x = x
    self.y = y
    
  def __init__(self, weapon, level, position):
    self.weapon = weapon
    self.level = level
    self.position = (x,y)

  