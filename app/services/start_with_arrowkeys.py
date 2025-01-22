import curses

def menu(stdscr):
    choices = ["Game_1", "Game_2"]
    selected = 0

    while True:
        stdscr.clear()
        stdscr.addstr("Use arrow keys to select a game to play:\n", curses.A_BOLD)
        
        for i, choice in enumerate(choices):
            if i == selected:
                stdscr.addstr(f"> {choice}\n", curses.A_REVERSE)  # Highlight selection
            else:
                stdscr.addstr(f"  {choice}\n")
                
        stdscr.refresh()
        
        key = stdscr.getch()

        if key == curses.KEY_UP and selected > 0:
            selected -= 1
        elif key == curses.KEY_DOWN and selected < len(choices) - 1:
            selected += 1
        elif key == ord("\n"):  # Enter key pressed
            return choices[selected]

choice = curses.wrapper(menu)
print(f"You selected: {choice}, let's play!")


