from minesweeperBoard import Board
import re
def play(dim_size=10, num_bombs=10):
    """
    Main game loop to play Minesweeper.

    Args:
        dim_size (int): Size of the board (default is 10).
        num_bombs (int): Number of bombs to place on the board (default is 10).
    """
    board = Board(dim_size, num_bombs)

    # Continue digging until all non-bomb locations are uncovered
    while len(board.dug) < board.dim_size ** 2 - num_bombs:
        print(board)
        user_input = re.split(r',\s*', input("Where would you like to dig? Input as row,col: "))

        # Validate input format
        if len(user_input) != 2:
            print("Invalid input. Please enter as row,col (e.g. 3,7)")
            continue

        try:
            row, col = int(user_input[0]), int(user_input[1])
            if row < 0 or row >= dim_size or col < 0 or col >= dim_size:
                raise ValueError
        except ValueError:
            print("Invalid input. Please enter valid integers within board range.")
            continue

        # Attempt to dig at the given location
        safe = board.dig(row, col)
        if not safe:
            break  # Bomb hit, game over

    # Game result
    if safe:
        print("CONGRATULATIONS! YOU WON!")
    else:
        print("GAME OVER!")
        # Reveal the full board after losing
        board.dug = {(r, c) for r in range(board.dim_size) for c in range(board.dim_size)}
        print(board)

# Entry point for the game
if __name__ == '__main__':
    play()
