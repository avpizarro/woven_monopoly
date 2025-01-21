class Board_Property():
  def __init__(self, name, type, price="None", colour="None"):
    self.name = name
    self.type = type
    self.colour = colour
    self.price = price
    self.rent = price

  def duplicate_rent(self):
    if isinstance(self.rent, int):
      self.rent *= 2
      print("New rent; ", self.rent)
      return self.rent
    else: 
      raise ValueError("Incorrect value")
