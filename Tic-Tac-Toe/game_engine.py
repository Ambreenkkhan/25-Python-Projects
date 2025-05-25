class TicTacToeGame:
    def __init__(self):
        # Create a board of 9 empty spaces
        self.board = [' ' for _ in range(9)]
        self.current_winner = None  # To track if someone has won

    def show_board(self):
        # Print the board in a 3x3 grid
        for row in [self.board[i*3:(i+1)*3] for i in range(3)]:
            print(' | ' + ' | '.join(row) + ' | ')

    @staticmethod
    def show_board_positions():
        # Display positions for player's reference
        positions = [[str(i) for i in range(j*3, (j+1)*3)] for j in range(3)]
        for row in positions:
            print(' | ' + ' | '.join(row) + ' | ')

    def get_valid_moves(self):
        # Return all indices that are still empty
        return [i for i, space in enumerate(self.board) if space == ' ']

    def has_empty_spaces(self):
        return ' ' in self.board

    def empty_count(self):
        return self.board.count(' ')

    def place_move(self, position, player_symbol):
        # Place the player's symbol on the board
        if self.board[position] == ' ':
            self.board[position] = player_symbol
            if self.check_win(position, player_symbol):
                self.current_winner = player_symbol
            return True
        return False

    def check_win(self, index, symbol):
        # Check row
        row_index = index // 3
        row = self.board[row_index*3:(row_index+1)*3]
        if all([spot == symbol for spot in row]):
            return True

        # Check column
        col_index = index % 3
        column = [self.board[col_index + i*3] for i in range(3)]
        if all([spot == symbol for spot in column]):
            return True

        # Check diagonals
        if index % 2 == 0:
            diagonal1 = [self.board[i] for i in [0, 4, 8]]
            if all([spot == symbol for spot in diagonal1]):
                return True
            diagonal2 = [self.board[i] for i in [2, 4, 6]]
            if all([spot == symbol for spot in diagonal2]):
                return True

        return False
