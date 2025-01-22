![Monopoly Board](assets/board_grayscale.PNG)

# 🏠 Woven Monopoly Game - Python

A simplified Monopoly-style game implemented in Python. Players roll dice, move around a virtual board, buy properties, pay rent, and aim to dominate the market! 🎲💰

##### Check final stats for both games here: [Roll_1](docs/rolls_1_stats.txt), [Roll_2](docs/rolls_2_stats.txt)
---

## 📜 Features
- 🎲 Dice rolling with randomized movement - coming soon
- 🏡 Buy and own properties
- 💸 Pay rent when landing on owned properties
- 👥 Multiplayer support
- 🔄 Dynamic game logic with win conditions

---

## 🚀 Installation

### 1️⃣ **Clone the repository**
```sh
git clone https://github.com/avpizarro/woven_monopoly.git
cd woven_monopoly
```

### 2️⃣ **Create a virtual environment (recommended)**
```sh
python3 -m venv venv
source venv/bin/activate  # Mac/Linux
venv\Scriptsctivate      # Windows
```

### 3️⃣ **Install dependencies**
```sh
pip3 install -r requirements.txt
```

### 4️⃣ **Run the game**
```sh
python3 app/main.py
```

### 4️⃣ **Test the game**
```sh
python3 -m unittest discover

```

---

## 🖼️ Game Logic Flowchart and Class Diagram

![Class Diagram and Flow Chart](assets/class_diagram_flowchart.png)

Before starting the project, I used Miro to map out the game's logic.
You can check the board here: [Miro Board](https://miro.com/app/board/uXjVLs9m8Mo=/?share_link_id=322083542266).

Visual aids, such as an actual image of the board, emojis, and icons, helped reinforce the logic.

I designed classes for players and properties, which will allow for easy expansion in the future—making it possible to add more players and properties.

I chose to focus on the game logic rather than the GUI, so I decided to build a command-line app using Python.

NOTE: requirements.txt is currently empty, but I am keeping it for future development.

---

## 🏗️ Project Structure

Starting with a simple structure, but I might look into adding **models and services** directories.

```sh
.
├── README.md                       # Project documentation
├── app                             # Main game package
│   ├── __init__.py
│   ├── board.py                    # Load the Board
│   ├── dice.py                     # Load the Rolls
│   ├── main.py                     # Game entry point
│   ├── models                      # Class constructors
│   │   ├── __init__.py
│   │   ├── board_property.py
│   │   └── player.py
│   ├── players.py                  # Load the players
│   └── services                    # Helper functions
│       ├── __init__.py
│       ├── create_rounds.py
│       ├── find_winner.py
│       └── start_with_arrowkeys.py
├── assets                          # Images, flowcharts, etc.
│   ├── board_grayscale.PNG
│   └── class_diagram_flowchart.png
├── data                            # Initial data
│   ├── board.json
│   ├── players.json
│   ├── rolls_1.json
│   └── rolls_2.json
├── docs                            # Game logs, stats and pseudocode
│   ├── pseudocode.txt
│   ├── rolls_1_log.txt
│   ├── rolls_1_stats.txt
│   ├── rolls_2_log.txt
│   └── rolls_2_stats.txt
├── requirements.txt
└── tests                           # Unit tests
    ├── __init__.py
    ├── test_Board_Property.py
    ├── test_create_rounds.py
    ├── test_find_winner.py
    └── test_player.py
```

---

## 🔮 Next Steps

- 🎲 **Randomized dice roll** to make the game interactive.
- 👥 **Add more players** and allow customization of initial wallet balance.
- 🏡 **Expand the board** by adding more properties.
- 🖥️ **Develop a GUI** using **Pygame**.

---

🎯 **Want to contribute?** Feel free to fork the repo, suggest improvements, or submit pull requests!  
🚀 Happy coding and enjoy the game! 🏡💰
