"""
Terminal Based connect 4 game
"""

BOARD_ROWS = 6
BOARD_COLUMNS = 7


class GameBoard():
    """
    Defines the game board values
    """
    def __init__(self):
        self.board = [[' ' for _ in range(BOARD_COLUMNS)]
                      for _ in range(BOARD_ROWS)]
        self.turn = 0
        self.last_move = [-1, -1]

    def print_board(self):
        """
        Adds column numbers and the prints the game board slots that
        players will insert their token into
        """
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
