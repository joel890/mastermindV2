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
    Checks the given option and chooses either the simple Shapiro strategy (option '1')
    or the full Knuth minimax strategy (option '2'). The chosen strategy is used to guess the
    mastercode.
    """
    if option == '1':
        return shapiro_strategy(mastercode)
    elif option == '2':
        return knuth_strategy(mastercode)
    else:
        print("Invalid option provided. Please select '1' for Shapiro strategy or '2' for Knuth strategy.")
        return None

def shapiro_strategy(mastercode):
    """
    Simple (Shapiro) strategy: Use the first consistent guess from the ordered list.
    """
    attempts = 0
    possible_combinations = all_combinations[:]  # copy of all possible combinations
    guess = possible_combinations[0] # first guess
    while attempts < 12:
        attempts += 1
        feedback = compare_code(mastercode, guess)
        print(f"Tries {attempts}: {guess} => Black pins: {feedback[0]}, White pins: {feedback[1]}")
        if feedback == (4, 0):
            print(f"Computer guessed the code: {guess} in {attempts} tries using Shapiro strategy!")
            return guess
        possible_combinations = [c for c in possible_combinations if is_consistent(c, guess, feedback)]
        if not possible_combinations:
            break
        guess = possible_combinations[0]
    print("Failed to guess the code within 12 attempts.")
    return None

def knuth_strategy(mastercode):
    """Knuth minimax strategy: selecting the guess that minimizes the maximum number of remaining possibilities."""
    attempts = 0
    S = all_combinations[:]  # copy of remaining solutions
    possible_guesses = all_combinations[:]  # all allowed guesses
    guess = [colors[0], colors[0], colors[1], colors[1]]  # first guess (AABB pattern)
    
    while True:
        feedback = compare_code(mastercode, guess)  # get feedback for current guess
        print(f"Tries {attempts}: {guess} => Black pins: {feedback[0]}, White pins: {feedback[1]}")  # display result
        
        if feedback == (4, 0):  # correct guess
            print(f"Computer guessed the code: {guess} in {attempts} tries using Knuth's strategy!")
            return guess
        
        S = [code for code in S if is_consistent(code, guess, feedback)]  # update remaining possibilities
        if not S:
            print("No consistent solution left.")
            return None
        
        min_score = float('inf')  # initialize worst-case count
        next_guess_candidates = []  # list for candidate guesses
        
        # Evaluate each possible guess from the full set
        for g in possible_guesses:
            counts = {}  # feedback count dictionary
            for code in S:
                r = compare_code(code, g)  # feedback if g would be the guess
                counts[r] = counts.get(r, 0) + 1  # count occurrences of this feedback
            worst = max(counts.values()) if counts else 0  # worst-case partition size for guess g
            
            if worst < min_score:
                min_score = worst  # new minimum worst-case found
                next_guess_candidates = [g]  # start new candidate list
            elif worst == min_score:
                next_guess_candidates.append(g)  # add equally good candidate
        
        chosen_guess = None
        # Prefer candidate that is in the set S of possible solutions
        for candidate in next_guess_candidates:
            if candidate in S:
                chosen_guess = candidate  # select candidate from S
                break
        if chosen_guess is None:
            chosen_guess = next_guess_candidates[0]  # fallback: choose first candidate
        
        guess = chosen_guess  # update guess for next iteration
        attempts += 1
