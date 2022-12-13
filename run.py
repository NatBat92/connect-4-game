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

    def turns(self):
        """
        creates the turns and the symbols of each player
        """
        players = ['#', '@']
        return players[self.turn % 2]

    def player_go(self, column):
        """
        determines the go has been completed by searching the column
        that was chosen for a change
        """
        # Search from the bottom of the column up
        for k in range(BOARD_ROWS-1, -1, -1):
            if self.board[k][column] == ' ':
                self.board[k][column] = self.turns()
                self.last_move = [k, column]

                self.turn += 1
                return True

        return False

    def in_grid(self, j, i):
        """
        checks if the players turn was a valid move
        inside the parameters of the game boad
        """
        return (j >= 0 and j < BOARD_ROWS and i >= 0 and i < BOARD_COLUMNS)

    def check_for_win(self):
        """
        checks the game board for 4 in a row to determine the end of the game
        """
        last_row = self.last_move[0]
        last_column = self.last_move[1]
        last_symbol = self.board[last_row][last_column]

        # [i, j] direction, matching symbol count
        win_directions = [
            [[-1, 0], 0, True],
            [[1, 0], 0, True],
            [[0, -1], 0, True],
            [[0, 1], 0, True],
            [[-1, -1], 0, True],
            [[1, 1], 0, True],
            [[-1, 1], 0, True],
            [[1, -1], 0, True],
        ]
