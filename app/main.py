# Load all the initial data
from board import board
from players import players
from dice import game_1, game_2

# Get the functions
from services.find_winner import find_winner

find_winner(players)


# print(board)
# print(players)
# print(game_1, game_2)
