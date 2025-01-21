class Player():
  def __init__(self, name):
    self.name = name
    self.wallet = 16 # All players start with 16 dollars
    self.location = 0 # All players start in 0
    self.realestate = [] # All players have no realstate at the start
  
  def credit(self, amount):
    """Add money to the wallet"""
    self.wallet += amount
    print(self.name, "your new balance is: ", self.wallet)
    return self.wallet
  
  def debit(self, amount):
    """Substract money from the wallet"""
    self.wallet -= amount
    print(self.name, "your new balance is: ", self.wallet)
    return self.wallet
  
  def set_location(self, roll):
    """Take the roll value and change the player's location, wich gives us
    an index to know where they are on the board"""
    new_location = self.location + roll
    
    if new_location <= 0 or roll <= 0 or roll > 6:
       return print("Incorrect value, roll again")
     
    elif new_location < 9:
      self.location = new_location
      
    else:
      self.location = new_location % 9
      self.wallet += 1
      
      print("You have completed a loop here is $1!")
    print("Your new location index is:", self.location)
    return self.location
  
  def new_realestate(self, property):
    """Add the property to the players realstate portfolio"""
    self.realestate.append(property)
    print("You have acquired:", property)
    print("Your realstate portfolio is growing:", self.realestate)
    return self.realestate
  
  
  
  
# alex = Player("Alex")
# alex.new_realestate("RMIT")
# alex.new_realestate("Central Park")
# alex.new_realestate("The Tan")

