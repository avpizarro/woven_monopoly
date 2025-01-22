def find_winner(players):
  """Find the winner, but first filter out the players with 0 dollars"""
  players_with_money = [ player for player in players if player.wallet > 0]
  
  #This shouldn't happen but make sure someone still has money to check for a winner
  if players_with_money == []:
    print("No one has money in this group! They are no winners!")
    return
  
  #Find the highest amount in wallet
  max_wallet = max(player.wallet for player in players_with_money)
  
  # Find all the players who have the max wallet amount, to account for ties
  winners = [player for player in players_with_money if player.wallet == max_wallet]
  
  if len(winners) == 1:
    winner = winners[0]
    print("And the winner, with", max_wallet, "left in their wallet is 🥁:", winner.name)
    return winner
  else:
    winning_players = ", ".join(player.name for player in winners)
    print("It's a tie! The winners with", max_wallet, "left in their wallet are 🥁:", winning_players)
    return winning_players  