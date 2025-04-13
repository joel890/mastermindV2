from mastermind_logic import generate_mastercode, pc_strategy, compare_code
from mastermind_ui import get_user_choice, check_player_input, ask_play_again

def player_vs_pc(mastercode):
    """
    Allow the player to guess the computer's mastercode.
    """
    tries = 0
    print("These are the colors to choose from: ", ['red', 'blue', 'green', 'yellow', 'white', 'black'])
    print(mastercode)  # Debug output 
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
    """
    Allow the computer to guess the player's mastercode.

    The player sets a secret mastercode, then chooses a strategy for the computer.
    The computer will try to guess the provided code.
    """
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
            break  # End the game loop

# Start the game
if __name__ == "__main__":
    run()
