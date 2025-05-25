import random

def play():
    """
    Main function to play a single round of Rock-Paper-Scissors
    Returns game result as a string
    """
    # Get user input and convert to lowercase
    user = input("What's your choice? 'r' for rock, 'p' for paper, 's' for scissors\n").lower()
    
    # Computer randomly selects from valid options
    computer = random.choice(['r', 'p', 's'])

    # Check for tie condition first
    if user == computer:
        return 'It\'s a tie'

    # Determine winner using game rules
    if is_win(user, computer):
        return 'You won!'

    # If not tie and user didn't win, user loses
    return 'You lost!'

def is_win(player, opponent):
    """
    Helper function to determine if player beats opponent
    Returns True if player wins, False otherwise
    Winning conditions:
    - Rock (r) beats Scissors (s)
    - Scissors (s) beats Paper (p)
    - Paper (p) beats Rock (r)
    """
    # Check all winning combinations
    if (player == 'r' and opponent == 's') or \
       (player == 's' and opponent == 'p') or \
       (player == 'p' and opponent == 'r'):
        return True
    return False  # Explicit return for clarity

# Start the game and print result
print(play())