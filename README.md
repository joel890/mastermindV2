# Mastermind Game

A Python implementation of the classic **Mastermind** game. Play as the codebreaker, or let the computer guess your secret code using smart strategies like Shapiro or Knuth.


## Running the Game

Start the game with:

python main.py


You’ll be asked to choose between different game modes:

- `1`: You try to guess the computer's code.
- `2`: The computer tries to guess your code using a strategy.
- `3`: Exit the game.

If you select option 2 (computer guesses your code), you’ll also choose a strategy:

- `1`: **Shapiro Strategy** – simple elimination method.
- `2`: **Knuth Strategy** – minimax algorithm for smarter guessing.

## Implemented Strategies

### 1. Shapiro Strategy
A basic elimination strategy. The computer picks the first valid guess from the remaining possibilities and filters based on feedback.

### 2. Knuth's Strategy
A smarter approach based on the minimax algorithm. It chooses guesses that minimize the worst-case number of remaining possibilities, often cracking the code in less than 5 tries. Crazy right

## Project Structure


main.py               # Game runner
mastermind_logic.py   # Game logic and algorithms
mastermind_ui.py      # User interaction and input
README.md             # You're here!


## Features

- Text-based interface
- Valid color checking
- Feedback after each guess (black and white pins)
- Two smart AI strategies
- Modular codebase with docstrings


## License

This project is licensed under the DToX Brand. Stay tuned for more later! ;)

## Author

Created by Joel Boafo – Studentnummer 1771818

