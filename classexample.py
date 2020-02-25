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

  def __init__(self, weapon, level, position, name):
    self.weapon = weapon
    self.level = level
    self.position = (x,y)
    self.name = name

  def position(self):
    self.x = ?
    self.y = ?

  

  def __repr__(self):
    return self.name

