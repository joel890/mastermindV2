import random
from itertools import product

colors = ['red', 'blue', 'green', 'yellow', 'white', 'black']  # all the colors possible in the mastercode
all_combinations = list(product(colors, repeat=4))  # all possible mastercode combinations


def generate_mastercode():
    master_code = random.choice(all_combinations)  # Randomly choose a combination from all_combinations
    return master_code


def get_user_choice():
    """
    This function presents the game options to the user and returns the user's choice.
    """
    while True:
        print("\nWelcome to the Mastermind Game!\n"
              "Choose Game option\n"
              "1: Guess the Code \n"
              "2: Make the computer guess \n"
              "3: Exit Game\n")
        option = input("Your choice: ")
        if option in ['1', '2', '3']:
            return option
        else:
            print("Invalid input, only options 1 or 2 are allowed\n")


def check_player_input():  # Check if the input has no typos
    while True:
        player_input = input("Enter your code (e.g., 'green,yellow,red,blue'): ")

        # Split the input by commas and remove whitespace to get a list of colors
        player_colors = [color.strip() for color in player_input.lower().split(',')]

        # Check if all entered colors are valid, only then return the list
        if all(color in colors for color in player_colors):
            return player_colors
        else:
            # Inform the player which color is not valid
            for color in player_colors:
                if color not in colors:
                    print(f"'{color}' is not a valid color. Try again.")


def compare_code(mastercode, player_guess):
    """"
    Here we give the feedback for the player's guess, check if they cracked the code or not.
    """
    white_pins = 0
    black_pins = 0

    # Keep record which positions are black
    correct_positions = []

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
    """
    Checks if a combination consistent is with the feedback with the current guess.
    """
    return compare_code(combination, guess) == feedback


def pc_strategy(mastercode, option):
    """
    Here the pc will try to crack the code with the given strategy from the player
    """
    attempts = 0
    possible_combinations = all_combinations[:]
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


def player_vs_pc(mastercode):
    tries = 0
    print("These are the colors to choose from: ", colors)
    print(mastercode)
    while tries < 12:
        player_guess = check_player_input()
        black_pins, white_pins = compare_code(mastercode, player_guess)
        tries += 1
        if black_pins == 4:
            print("You guessed the code!\nAmount of tries: ", tries)
            break
        else:
            print("Not quite try again! white pins: ", white_pins, " Black pins: ", black_pins)

    play_again = ask_play_again()
    if play_again == 'yes':
        player_vs_pc(generate_mastercode())
    else:
        return  # back to menu


def pc_vs_player():
    while True:
        print("Enter a mastercode for the computer to guess.")
        player_code = check_player_input()
        option = input("Choose the pc's strategy:\n 1: Shapiro Strategy\n 2: Knuth Strategy??\n Your choice: ")
        if option in ['1', '2']:
            pc_strategy(player_code, option)
            play_again = ask_play_again()
            if play_again == 'yes':
                continue
            else:
                break
        else:
            print("Invalid input, only options 1 or 2 are allowed\n")


def ask_play_again():
    while True:
        play_again = input("Play again? (yes/no): ").lower().strip()
        if play_again in ['yes', 'no']:
            return play_again
        else:
            print("Invalid input. Please answer 'yes' or 'no'.")


def run():
    """
    This is the main driver function that runs the game loop.
    """
    while True:
        mastercode = generate_mastercode()
        user_choice = get_user_choice()  # Get the user's game option choice

        if user_choice == '1':
            player_vs_pc(mastercode)
        elif user_choice == '2':
            pc_vs_player()
        elif user_choice == '3':
            print("Exiting game. Thanks for playing!")
            break  # Exit the loop, thus ending the game


# Start the game
run()
