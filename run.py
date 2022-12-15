import pyinputplus as pyip
from pyfiglet import Figlet
f = Figlet(font='5lineoblique')


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
        players_symbols = ['#', '@']
        return players_symbols[self.turn % 2]

    def player_go(self, column):
        """
        determines the go has been completed by searching the column
        that was chosen for a change
        """
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

        # search all directions 4 spaces for matching symbols
        for b in range(4):
            for m in win_directions:
                j = last_row + (m[0][0] * (b+1))
                i = last_column + (m[0][1] * (b+1))

                if m[2] and self.in_grid(j, i) and self.board[j][i]\
                   == last_symbol:
                    m[1] += 1
                else:
                    # Stop searching that direction if a win isn't found
                    m[2] = False

        # Check possible direction pairs for '4 in a row'
        for a in range(0, 7, 2):
            if win_directions[a][1] + win_directions[a+1][1] >= 3:
                self.print_board()
                print(f"{last_symbol} is the winner!")
                play_again = str(input("do you want to play again? "
                                       "(type 'y' for yes and 'n' for no): "))
                if play_again == 'y':
                    play_game()
                else:
                    print("thank you for playing!")
                return last_symbol

        # no win found
        return False


class Player():
    """
    Gets player name input
    """
    player_one_name = pyip.inputStr(prompt="Enter the name for player 1: ",
                                    blank=False, blockRegexes=[r'([0-9])'])

    player_two_name = pyip.inputStr(prompt="Enter the name for player 2: ",
                                    blank=False, blockRegexes=[r'([0-9])'])
    print("\n")
    print(f"{player_one_name} = '#'         {player_two_name} = '@'", "\n")


def play_game():
    """
    Runs the game and checks for a win at the end
    """
    game = GameBoard()
    game_over = False
    while not game_over:
        # Game to continue

        game.print_board()

        valid_drop = False
        while not valid_drop:
            player_move = pyip.inputInt(f"{game.turns()} 's turn, "
                                        f"please pick a column 1-7: ",
                                        blank=False, min=1, max=7)
            valid_drop = game.player_go(int(player_move)-1)

        game_over = game.check_for_win()

        if not any(' ' in x for x in game.board):
            print("This is a tie")
            return


if __name__ == '__main__':
    print(f.renderText('Connect 4'))
    Player()
    play_game()
