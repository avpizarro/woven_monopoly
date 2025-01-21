import json
import os

#Get absolute path to JSON files
json_path_1 = os.path.join(os.path.dirname(__file__), "..", "data", "rolls_1.json")
json_path_2 = os.path.join(os.path.dirname(__file__), "..", "data", "rolls_2.json")

# Load the rolls_1.json file
with open(json_path_1, "r") as file:
  game1 = json.load(file) # Convert JSON to Python list

# Load the rolls_2.json file
with open(json_path_2, "r") as file:
  game2 = json.load(file) # Convert JSON to Python list