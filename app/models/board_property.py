class Board_Property():
  def __init__(self, name, price, colour, type):
    self.name = name
    self.colour = colour
    self.type = type
    self.price = price
    self.rent = price

  def duplicate_rent(self):
    if isinstance(self.rent, int):
      self.rent *= 2
      print("New rent; ", self.rent)
      return self.rent
    else: 
      raise ValueError("Incorrect value")
  

house = Board_Property("lagenda", "2", "red", "property")
print(house.duplicate_rent())