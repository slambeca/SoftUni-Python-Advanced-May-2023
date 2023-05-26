directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1),
}

n = int(input())

matrix = []
# [['1', 'X', '7', '9', '11'],
# ['X', '14', '46', '62', '0'],
# ['15', '33', '21', '95', 'X'],
# ['P', '14', '3', '4', '18'],
# ['9', '20', '33', 'X', '0']]

player_row, player_column = 0, 0

for row in range(n):
    current_row = input().split()
    matrix.append(current_row)

    if "P" in current_row:
        player_row, player_column = row, current_row.index("P")

path = [[player_row, player_column]]

GOAL = 100
total_collected_coins = 0
game_won = False

while not game_won:
    command = input()
    if command not in ["up", "down", "left", "right"]:
        continue

    matrix[player_row][player_column] = 0
    player_row += directions[command][0]
    player_column += directions[command][1]

    if player_row < 0:
        player_row = n - 1
    elif player_row == n:
        player_row = 0

    if player_column < 0:
        player_column = n - 1
    elif player_column == n:
        player_column = 0

    symbol = matrix[player_row][player_column]

    path.append([player_row, player_column])

    if symbol == "X":
        total_collected_coins = int(total_collected_coins / 2)
        break
    elif str(symbol).isnumeric():
        total_collected_coins += int(symbol)

    matrix[player_row][player_column] = 0

    if total_collected_coins >= GOAL:
        game_won = True
        break

if game_won:
    print(f"You won! You've collected {total_collected_coins} coins.")
else:
    print(f"Game over! You've collected {total_collected_coins} coins.")

print("Your path:")
[print(el) for el in path]

# Variant 2
# n = int(input())
#
# matrix = []
# # 1 X 7 9 11
# # X 14 46 62 0
# # 15 33 21 95 X
# # P 14 3 4 18
# # 9 20 33 X 0
#
# directions = {
#     "up": (-1, 0),
#     "down": (1, 0),
#     "left": (0, -1),
#     "right": (0, 1),
# }
#
# player_position = []    # [3, 0]
# player_path = []
# collected_coins = 0
# game_won = False
#
# for row in range(n):
#     matrix.append(input().split())
#
#     if "P" in matrix[row]:
#         player_position = [row, matrix[row].index("P")]
#         matrix[row][player_position[1]] = "0"    # We clean the position of the player
#         player_path.append(player_position)
#
#
# while True:
#     command = input()    # left
#
#     if command in directions.keys():
#         wanted_row = player_position[0] + directions[command][0]
#         wanted_col = player_position[1] + directions[command][1]
#
#         if wanted_row < 0:
#             wanted_row = n - 1
#         elif wanted_row == n:
#             wanted_row = 0
#
#         if wanted_col < 0:
#             wanted_col = n - 1
#         elif wanted_col == n:
#             wanted_col = 0
#
#         current_position = matrix[wanted_row][wanted_col]
#
#         if current_position.isdigit():
#             collected_coins += int(current_position)
#             matrix[wanted_row][wanted_col] = "0"
#             player_path.append([wanted_row, wanted_col])
#             player_position = [wanted_row, wanted_col]
#
#             if collected_coins >= 100:
#                 print(f"You won! You've collected {collected_coins} coins.")
#                 game_won = True
#                 break
#         elif current_position == "X":
#             player_path.append([wanted_row, wanted_col])
#             player_position = [wanted_row, wanted_col]
#             break
#
# if not game_won:
#     print(f"Game over! You've collected {collected_coins // 2} coins.")
# print("Your path:")
# for path in player_path:
#     print(path)