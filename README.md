# Slot Machine Game

This is a simple console-based slot machine game implemented in Python. The game allows the player to bet on multiple lines and spin the slot machine to see if they win any prizes.

## How to Play

1. The player starts with a default balance.
2. The player can choose the number of lines they want to bet on (1-3).
3. The player then places a bet (between $1 and $200).
4. The slot machine spins, displaying the results.
5. The player wins if they get matching symbols on any bet lines.

## Features

- The game keeps track of the player's balance and updates it after each spin.
- The player can quit the game at any time by pressing 'q'.
- If the player runs out of balance, they can choose to deposit more money to continue playing.
- The game checks if the entered values are valid and prompts the user for correct input if needed.

## Customization

You can customize the game by changing the following variables:
- `MAX_LINES`: Maximum number of bet lines allowed.
- `MAX_BETS`: Maximum bet amount allowed.
- `MIN_BETS`: Minimum bet amount allowed.
- `ROWS` and `COLS`: Define the grid dimensions of the slot machine.
- `symbol_count`: Dictionary representing the count of each symbol.
- `symbol_values`: Dictionary representing the value of each symbol.

## How to Run

1. Ensure you have Python installed on your system.
2. Copy and paste the code into a Python file (e.g., `slot_machine.py`).
3. Run the file using a Python interpreter.

Have fun playing the game!
