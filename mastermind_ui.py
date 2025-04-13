def get_user_choice():
    """Present the game options to the user and return the user's choice."""
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

def check_player_input():
    """Prompt for and validate the player's code input.

    Splits the user input (e.g., 'green,yellow,red,blue') by commas, strips extra whitespace,
    and checks that all entered colors are valid.
    
    Returns:
        A list of valid colors as entered by the player.
    """
    valid_colors = ['red', 'blue', 'green', 'yellow', 'white', 'black']
    while True:
        player_input = input("Enter your code (e.g., 'green,yellow,red,blue'): ")

        # Split the input by commas and remove whitespace to get a list of colors
        player_colors = [color.strip() for color in player_input.lower().split(',')]

        # Check if all entered colors are valid, only then return the list
        if all(color in valid_colors for color in player_colors):
            return player_colors
        else:
            # Inform the player which color is not valid
            for color in player_colors:
                if color not in valid_colors:
                    print(f"'{color}' is not a valid color. Try again.")

def ask_play_again():
    """
    Ask the player if they want to play again.
    """
    while True:
        play_again = input("Play again? (yes/no): ").lower().strip()
        if play_again in ['yes', 'no']:
            return play_again
        else:
            print("Invalid input. Please answer 'yes' or 'no'.")
