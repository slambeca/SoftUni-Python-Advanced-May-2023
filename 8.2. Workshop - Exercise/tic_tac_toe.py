from collections import deque
from colorama import Fore
from pyfiglet import Figlet


def check_for_win():
    player_name, player_symbol = players[0]

    first_diagonal_win = all([board[i][i] == player_symbol for i in range(SIZE)])
    second_diagonal_win = all([board[i][SIZE - i - 1] == player_symbol for i in range(SIZE)])

    row_win = any([all(player_symbol == pos for pos in row) for row in board])
    col_win = any([all(board[r][c] == player_symbol for r in range(SIZE)) for c in range(SIZE)])

    if any([first_diagonal_win, second_diagonal_win, row_win, col_win]):
        print_board()
        print(Fore.CYAN + f"{player_name} won! Congratulations!" + Fore.RESET)

        raise SystemExit


def place_symbol(row, col):
    board[row][col] = players[0][1]

    check_for_win()
    print_board()    # No need for parameter "begin"

    if turns == SIZE * SIZE:
        print(Fore.RED + "Draw!" + Fore.RESET)
        raise SystemExit

    players.rotate()


def choose_position():
    global turns

    while True:
        try:
            position = int(input(f"{players[0][0]}, choose a free position in the range [1-{SIZE * SIZE}]: "))
            row, col = (position - 1) // SIZE, (position - 1) % SIZE
        except ValueError:
            print(Fore.RED + f"{players[0][0]}, please select a valid position!" + Fore.RESET)
            continue

        if 1 <= position <= SIZE * SIZE and board[row][col] == " ":
            turns += 1
            place_symbol(row, col)
        else:
            print(Fore.RED + f"{players[0][0]}, please select a valid position! "
                             f"This position is invalid or already taken!" + Fore.RESET)


def print_board(begin=False):
    if begin:
        print("\nThe board looks like this:")
        [print(Fore.LIGHTGREEN_EX + f"| {' | '.join(row)} |" + Fore.RESET) for row in board]

        for row in range(SIZE):
            for col in range(SIZE):
                board[row][col] = " "

    else:
        [print(f"| {' | '.join(row)} |") for row in board]


def start():
    figlet = Figlet(font="ogre")
    print(figlet.renderText("Tic-Tac-Toe"))

    player_one_name = input("Player one, please enter your name: ").title()
    player_two_name = input("Player two, please enter your name: ").title()
    print(f"\n*** Hello, {player_one_name} and {player_two_name}! ***\n")

    while True:
        player_one_symbol = input(f"{player_one_name}, would you like to play with 'X' or 'O')? ").upper()

        if player_one_symbol not in ["X", "O"]:
            print(Fore.RED + f"{player_one_name}, please select a valid option!" + Fore.RESET)

        else:
            print(Fore.BLUE + f"{player_one_name} selected {player_one_symbol}!" + Fore.RESET)
            player_two_symbol = "O" if player_one_symbol == "X" else "X"
            print(Fore.BLUE + f"{player_two_name} will play with {player_two_symbol}!" + Fore.RESET)
            break

    players.append([player_one_name, player_one_symbol])
    players.append([player_two_name, player_two_symbol])

    print_board(begin=True)
    choose_position()


SIZE = 3
turns = 0

board = [[str(i), str(i + 1), str(i + 2)] for i in range(1, SIZE * SIZE + 1, SIZE)]
# ['1', '2', '3']
# ['4', '5', '6']
# ['7', '8', '9']

players = deque()    # deque([['Benjamin', 'X'], ['George', 'O']])

start()
print_board()