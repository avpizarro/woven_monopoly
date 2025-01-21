import json
import os

from models.player import Player

#Get absolute path to JSON file
json_path = os.path.join(os.path.dirname(__file__), "..", "data", "players.json")

# Load the players.json file
with open(json_path, "r") as file:
  players_data = json.load(file) # Convert JSON to Python list of dictionaries

# Use Playerclass to turn each player into an instance so they have their wallet, location and realestate portfolio
players = [ Player(**player) for player in players_data ]