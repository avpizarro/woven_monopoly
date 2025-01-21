class Board_Property():
  def __init__(self, name, price, colour, type):
    self.name = name
    self.colour = colour
    self.type = type
    self.price = price
    self.rent = price

  def duplicate_rent(self):
    return int(self.rent) * 2
  

house = Board_Property("lagenda", "2", "red", "property")
print(house.duplicate_rent())