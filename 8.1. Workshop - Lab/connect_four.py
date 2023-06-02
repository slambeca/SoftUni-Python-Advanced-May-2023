from collections import deque
from colorama import Fore


def print_func(some_array):
    [print(f"[ {', '.join(row)} ]") for row in some_array]


def check_indices(c, n):
    if 0 <= c < n:
        return True

    return False


def place_symbol():
    row = 0

    while row != ROWS and playing_board[row][player_column] == "0":
        row += 1

    playing_board[row - 1][player_column] = player_symbol

    return row - 1


def check_for_win(r, c):
    for x, y in directions:
        count = 1

        for i in range(1, 4):
            new_row = r + x * i
            new_col = c + y * i

            if not (0 <= new_row < ROWS and 0 <= new_col < COLUMNS) or playing_board[new_row][new_col] != player_symbol:
                break

            count += 1

        for i in range(1, 4):
            new_row = r - x * i
            new_col = c - y * i

            if not (0 <= new_row < ROWS and 0 <= new_col < COLUMNS) or playing_board[new_row][new_col] != player_symbol:
                break

            count += 1

        if count >= 4:
            return True

    if counter_for_draw == ROWS * COLUMNS:
        print(Fore.YELLOW + "*** Draw! ***" + Fore.RESET)
        print_func(playing_board)
        raise SystemExit

    return False


ROWS, COLUMNS = 6, 7

counter_for_draw = 0

playing_board = [["0"] * COLUMNS for row in range(ROWS)]
# ['0', '0', '0', '0', '0', '0', '0']
# ['0', '0', '0', '0', '0', '0', '0']
# ['0', '0', '0', '0', '0', '0', '0']
# ['0', '0', '0', '0', '0', '0', '0']
# ['0', '0', '0', '0', '0', '0', '0']
# ['0', '0', '0', '0', '0', '0', '0']

player_one_symbol = Fore.GREEN + "X" + Fore.RESET
player_two_symbol = Fore.BLUE + "Y" + Fore.RESET

turns = deque([[1, player_one_symbol], [2, player_two_symbol]])

directions = (
    (-1, 0),
    (0, -1),
    (-1, -1),
    (-1, 1,),
)

game_won = False

while not game_won:
    [print(f"[ {', '.join(row)} ]") for row in playing_board]

    player_number, player_symbol = turns[0]

    try:
        player_column = int(input(Fore.CYAN + f"Player {player_number}, please choose a column: " + Fore.RESET)) - 1
    except ValueError:
        print(Fore.RED + f"Invalid input! Please select a valid number in the range from 1 to {COLUMNS}!" + Fore.RESET)
        continue

    if not check_indices(player_column, COLUMNS):
        print(Fore.RED + f"Invalid input! Please select a valid number in the range from 1 to {COLUMNS}!" + Fore.RESET)
        continue

    if playing_board[0][player_column] != "0":
        print(Fore.RED + "Please choose another column, there is no space left in that one!" + Fore.RESET)
        continue

    row = place_symbol()
    counter_for_draw += 1
    win = check_for_win(row, player_column)

    turns.rotate()

    if win:
        break

print(f"\n***** Player {turns[1][0]} wins! Congratulations! *****\nThe final state of the playing board is:\n")
print_func(playing_board)