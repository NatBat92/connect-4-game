"""
Terminal Based connect 4 game
"""

BOARD_ROWS = 6
BOARD_COLUMNS = 7

class GameBoard():

    def __init__(self):
        self.board = [[' ' for _ in range(BOARD_COLUMNS)] for _ in range(BOARD_ROWS)]
        self.turn = 0
        self.last_move = [-1, -1] # row, column

    def print_board(self):
        # Add column numbers
        print("\n")
        for i in range(BOARD_COLUMNS):
            print(f" ({i + 1}) ", end="")
        print("\n")

        # Print the slots of the board
        for j in range(BOARD_ROWS):
            print('|', end="")
            for i in range(BOARD_COLUMNS):
                print(f"  {self.board[j][i]} |", end="")
            print("\n")

        print(f"{'-' * 35}\n")