import random
import re

class Board:
    def __init__(self, dim_size, num_bombs):
        """
        Initialize the board with the specified dimensions and number of bombs.
        """
        self.dim_size = dim_size
        self.num_bombs = num_bombs

        # Create the board and assign values to each cell
        self.board = self.make_new_board()
        self.assign_values_to_board()

        # Keep track of locations the user has already dug
        self.dug = set()

    def make_new_board(self):
        """
        Create a new board and randomly plant bombs.
        """
        board = [[None for _ in range(self.dim_size)] for _ in range(self.dim_size)]
        bombs_planted = 0

        # Randomly place bombs until the desired count is reached
        while bombs_planted < self.num_bombs:
            loc = random.randint(0, self.dim_size ** 2 - 1)
            row = loc // self.dim_size
            col = loc % self.dim_size

            # Avoid placing more than one bomb in the same cell
            if board[row][col] == '*':
                continue

            board[row][col] = '*'
            bombs_planted += 1

        return board

    def assign_values_to_board(self):
        """
        Assign a number to each cell based on the count of neighboring bombs.
        """
        for r in range(self.dim_size):
            for c in range(self.dim_size):
                if self.board[r][c] == '*':
                    continue
                self.board[r][c] = self.get_num_neighboring_bombs(r, c)

    def get_num_neighboring_bombs(self, row, col):
        """
        Count the number of bombs adjacent to the given cell.
        """
        num_bombs = 0
        for r in range(max(0, row - 1), min(self.dim_size, row + 2)):
            for c in range(max(0, col - 1), min(self.dim_size, col + 2)):
                if r == row and c == col:
                    continue
                if self.board[r][c] == '*':
                    num_bombs += 1
        return num_bombs

    def dig(self, row, col):
        """
        Recursively dig at the given location. Return False if a bomb is hit, True otherwise.
        """
        self.dug.add((row, col))

        # Hit a bomb
        if self.board[row][col] == '*':
            return False
        # Dig next to a bomb, stop digging further
        elif self.board[row][col] > 0:
            return True

        # Recursively dig neighboring cells if current cell is 0
        for r in range(max(0, row - 1), min(self.dim_size, row + 2)):
            for c in range(max(0, col - 1), min(self.dim_size, col + 2)):
                if (r, c) in self.dug:
                    continue
                self.dig(r, c)

        return True

    def __str__(self):
        """
        Return a string representation of the board showing only the dug locations.
        """
        visible_board = [[None for _ in range(self.dim_size)] for _ in range(self.dim_size)]

        for r in range(self.dim_size):
            for c in range(self.dim_size):
                if (r, c) in self.dug:
                    visible_board[r][c] = str(self.board[r][c])
                else:
                    visible_board[r][c] = ' '

        # Build a formatted string representation of the board
        string_rep = '   ' + '  '.join([str(i) for i in range(self.dim_size)]) + '\n'
        string_rep += '-' * (self.dim_size * 3 + 3) + '\n'
        for i in range(self.dim_size):
            row = visible_board[i]
            string_rep += f"{i} |" + ' |'.join(row) + ' |\n'
        string_rep += '-' * (self.dim_size * 3 + 3)
        return string_rep
