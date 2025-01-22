import curses

# Load all the initial data
from board import board
from players import players
from dice import game_1, game_2

# Get the functions
from services.start_with_arrowkeys import menu
from services.find_winner import find_winner

selected_option = curses.wrapper(menu)

if selected_option == "Game_1":
  game = game_1
else:
  game = game_2
  