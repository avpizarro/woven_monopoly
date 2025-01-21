import json
import os

from models.board_property import Board_Property

#Get absolute path to JSON file
json_path = os.path.join(os.path.dirname(__file__), "..", "data", "board.json")

# Load the Board.json file
with open(json_path, "r") as file:
  board_data = json.load(file) # Convert JSON to Python list of dictionaries

# Use Board_Property class to turn each property into an instance
board = [ Board_Property(**property) for property in board_data ]
