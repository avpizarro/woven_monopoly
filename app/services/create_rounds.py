def create_rounds(game, players):
  """Split the array that contains the dice values into a list of rounds"""
  dice_values = game
  round_length = len(players)
  
  #Initialise list to store each round
  rounds = list()
    
  while len(dice_values) > 0:
  
    round = dice_values[:round_length]
    rounds.append(round)
    del dice_values[:round_length]
  
  return rounds