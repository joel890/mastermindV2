import random
from itertools import product

colors = ['red', 'blue', 'green', 'yellow', 'white', 'black']  # all the colors possible in the mastercode
all_combinations = list(product(colors, repeat=4))  # all possible mastercode combinations

def generate_mastercode():
    """Generate a random master code from all possible combinations."""
    master_code = random.choice(all_combinations)  # Randomly choose a combination from all_combinations
    return master_code

def compare_code(mastercode, player_guess):
    """
    Provide feedback for the player's guess by comparing it with the mastercode.
    Return a tuple of black and white pins.
    """
    white_pins = 0
    black_pins = 0

    # Keep record which positions are black
    correct_positions = []  # indices with correct color and position

    # Check if the color is in the correct position
    for index, (master, guess) in enumerate(zip(mastercode, player_guess)):
        if master == guess:
            black_pins += 1
            correct_positions.append(index)

    # Make copies that remove the correct position from the list
    master_remaining = [mastercode[i] for i in range(len(mastercode)) if i not in correct_positions]
    guess_remaining = [player_guess[i] for i in range(len(player_guess)) if i not in correct_positions]

    # Check if the color is in the remaining list
    for color in guess_remaining:
        if color in master_remaining:
            white_pins += 1
            master_remaining.remove(color)  # delete so you get accurate number of pins

    return black_pins, white_pins

def is_consistent(combination, guess, feedback):
    """Check if a combination is consistent with the provided feedback for the current guess."""
    return compare_code(combination, guess) == feedback

def pc_strategy(mastercode, option):
    """
    The computer tries to crack the code using the given strategy.
    """
    attempts = 0
    possible_combinations = all_combinations[:]  # copy of all possible combinations
    if option == '1':
        guess = possible_combinations[0]  # Choose the first guess of the list
    else:
        guess = [colors[0], colors[0], colors[1], colors[1]]  # Choose the first 2 colors for the AABB effect.
    while attempts < 12:
        attempts += 1
        feedback = compare_code(mastercode, guess)

        print(f"Tries {attempts}: {guess} => Black pins: {feedback[0]}, White pins: {feedback[1]}")

        if feedback == (4, 0):
            print(f"You guessed the code: {guess} in {attempts} tries!")
            return guess

        # Only keep the combinations that suit the given feedback
        possible_combinations = [c for c in possible_combinations if is_consistent(c, guess, feedback)]
        guess = possible_combinations[0]
