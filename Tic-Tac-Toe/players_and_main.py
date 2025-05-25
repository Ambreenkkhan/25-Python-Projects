import random
from game_engine import TicTacToeGame

# Base player class
class Player:
    def __init__(self, symbol):
        self.symbol = symbol

    def select_move(self, game):
        pass


# Human player class
class HumanPlayer(Player):
    def select_move(self, game):
        # Ask user for input until a valid move is given
        move_valid = False
        choice = None
        while not move_valid:
            move = input(f"{self.symbol}'s turn. Choose a position (0-8): ")
            try:
                choice = int(move)
                if choice not in game.get_valid_moves():
                    raise ValueError
                move_valid = True
            except ValueError:
                print("Invalid move. Please select an empty position (0-8).")
        return choice

# Random computer player class
class ComputerPlayer(Player):
    def select_move(self, game):
        # Choose a move randomly from available ones
        return random.choice(game.get_valid_moves())


# Game controller function
def run_game(game, player_x, player_o, display=True):
    if display:
        print("Board positions:")
        game.show_board_positions()

    current_symbol = 'X'

    while game.has_empty_spaces():
        if current_symbol == 'X':
            position = player_x.select_move(game)
        else:
            position = player_o.select_move(game)

        if game.place_move(position, current_symbol):
            if display:
                print(f"\n{current_symbol} places at position {position}")
                game.show_board()
                print()

            if game.current_winner:
                print(f"{current_symbol} wins the game! 🎉")
                return current_symbol

            # Switch turns
            current_symbol = 'O' if current_symbol == 'X' else 'X'

    if display:
        print("It's a draw!")


# Main block
if __name__ == "__main__":
    player_x = HumanPlayer('X')
    player_o = ComputerPlayer('O')
    game_instance = TicTacToeGame()
    run_game(game_instance, player_x, player_o)
