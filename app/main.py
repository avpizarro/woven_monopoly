import curses
from time import sleep

# Load all the initial data
from board import board
from players import players
from dice import game_1, game_2

# Get the functions
from services.start_with_arrowkeys import menu
from services.create_rounds import create_rounds
from services.find_winner import find_winner

selected_option = curses.wrapper(menu)

# Set the chosen game list after user chooses
if selected_option == "Game_1":
  game = game_1
else:
  game = game_2
  
# Create the rounds
rounds = create_rounds(game, players)

game_over = False
  
# Loop to play each round
for i in range(len(rounds)):

  print("------------------------- ROUND", i+1, "--------------------------")
  
  for player in players:
    realestate = []
    if player.realestate != []:
      for property in player.realestate:
        realestate.append(property.name)
    print(player.name, "has", player.wallet, "and owns:", realestate)
  
  round = rounds[i]
  
  # Loop through the round
  for j in range(len(round)):
    if game_over: # Stop immediately if game_over is triggered
      break
    
    sleep(0.25)
    
    print("********************** NEXT PLAYER ********************")
    
    sleep(0.25)
    # Get each player and the dice value they rolled to play their turn
    player = players[j]
    roll = round[j]
    
    print(player.name.capitalize(), "rolled", roll)
    
    sleep(0.25)
    
    # Move the player
    location_index = player.set_location(roll)
    location = board[location_index]
    print(player.name.capitalize(), "is in:", location.name)
    
    sleep(0.25)
    if location.owner is None:
      print(location.name, "belongs to nadie!")
    else:
      print(location.name, "belongs to", location.owner.name)
  
    sleep(0.25)
    
    # Player is the GO tile (Already credited 1 when setting new_location)
    if location_index == 0:
      continue # NEXT PLAYER turn
      
    # Property has no owner: BUY IT
    elif location.owner is None:
      
      # Case if the player ends up with 0 dollars
      if player.wallet <= location.price:
        player.debit(location.price)
        print("GAME OVER", player.name, "is broke!")
        sleep(0.25)
        game_over = True # GAME OVER
        break
      
      # Case if the player has enough money to buy
      else: 
        player.debit(location.price)
        sleep(0.25)
        player.new_realestate(location)
        sleep(0.25)
        location.add_owner(player)
        
        # Check if the rent needs to be increased
        if len(player.realestate) <= 1 or location.rent > location.price:
          sleep(0.25)
          continue # NEXT PLAYER
        else: 
          colour_to_check = location.colour
          properties_to_increase = []
          # Loop through the realestate portfolio of the customer and get all the colours
          for item in player.realestate:
            if item.colour == colour_to_check:
              properties_to_increase.append(item)
          
          if len(properties_to_increase) == 2:
            properties_to_increase[0].duplicate_rent()
            properties_to_increase[1].duplicate_rent()
            print("Rent increased for:", properties_to_increase[0].name, properties_to_increase[1].name)  
            
          sleep(0.25)                    
    # Property has an owner: PAY RENT
    else:
      print("You need to pay", location.rent)
      if player.wallet <= location.rent:
        
        # Debit the passer by and check if they loose
        player.debit(location.rent)
        
        # Credit the owner whatever is left in the wallet
        location.owner.credit(player.wallet)
        print("GAME OVER", player.name, "is broke!")
        game_over = True # GAME OVER
        break
        
      else:
        player.debit(location.rent)
        location.owner.credit(location.rent)
        print(location.owner.name, "you received a payment of:", location.rent, "for", location.name)
  
  
  if game_over: 
    break
  
sleep(0.25)
find_winner(players)

print("********************** GAME STATS ********************")

#Print Stats
for player in players:
  player.print_info(board)

#THE END