class Board_Property():
  def __init__(self, name, type, price="None", colour="None"):
    self.name = name
    self.type = type
    self.price = price
    self.colour = colour
    self.rent = price
    self.owner = None

  # Method to duplicate the rent that can be used when a player owns two properties of the same colour
  def duplicate_rent(self):
    if isinstance(self.rent, int):
      self.rent *= 2
      return self.rent
    else: 
      raise ValueError("Incorrect value")
  
  #Method to buy the property
  def add_owner(self, player):
    self.owner = player
    print("The new owner of", self.name, "is", player.name)
    return self.owner
    
