def check_valid_index(row, col, player=False):  # If the indexes are invalid and we are checking the players indexes,
    # that means he won the game
    global game_won
    if 0 <= row < rows and 0 <= col < cols:
        return True
    if player:
        game_won = True


def bunnies_positions():
    positions = []

    for row in range(rows):
        for col in range(cols):
            if matrix[row][col] == "B":
                positions.append([row, col])

    return positions  # [[2, 3]]


def bunnies_move(bunnies_pos):
    # We iterate through all the bunnies
    for row, col in bunnies_pos:  # [2, 3]
        for bunnie_move in directions.values():
            new_row, new_col = row + bunnie_move[0], col + bunnie_move[1]

            if check_valid_index(new_row, new_col):
                matrix[new_row][new_col] = "B"


def show_results(status="won"):
    [print(*row, sep="") for row in matrix]
    print(f"{status}: {player_row} {player_col}")

    raise SystemExit


def check_player_alive(row, col):
    if matrix[row][col] == "B":
        show_results("dead")


rows, cols = [int(x) for x in input().split()]  # 5 6

matrix = [list(input()) for _ in range(rows)]  # ['.', '.', '.', '.', '.', 'P']
# . . . . . P
# . . . . . .
# . . . B . .
# . . . . . .
# . . . . . .

commands = input()

game_won = False

directions = {
    "U": (-1, 0),
    "D": (1, 0),
    "L": (0, -1),
    "R": (0, 1),
}
# player_row = player_row + directions["U"][0]
# player_col = player_col + directions["U"][1]

player_row, player_col = 0, 0

# To find the position of the player
for row in range(rows):
    if "P" in matrix[row]:
        player_row, player_col = (row, matrix[row].index("P"))

matrix[player_row][player_col] = "."  # To remove the player from the map
# . . . . . .
# . . . . . .
# . . . B . .
# . . . . . .
# . . . . . .

for command in commands:
    # We are not yet moving the player
    player_movement_row, player_movement_col = player_row + directions[command][0], player_col + directions[command][1]

    if check_valid_index(player_movement_row, player_movement_col, True):
        player_row, player_col = player_movement_row, player_movement_col

    bunnies_move(bunnies_positions())

    if game_won:
        show_results()

    check_player_alive(player_row, player_col)