size = int(input())

directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1),
}

battle_cruisers_destroyed = 0
mines_hit = 0

matrix = []
# * - - * -
# - S - * C
# - * - - -
# - - - - -
# - C - * C

submarine_position = []    # [1, 1]

for row in range(size):
    matrix.append([x for x in input()])    # We use comprehension when there are no spaces

    if "S" in matrix[row]:
        submarine_position = [row, matrix[row].index("S")]
        matrix[row][submarine_position[1]] = "-"

while True:
    direction = input()    # right

    wanted_row = submarine_position[0] + directions[direction][0]    # 1
    wanted_col = submarine_position[1] + directions[direction][1]    # 2

    if matrix[wanted_row][wanted_col] == "-":
        submarine_position = [wanted_row, wanted_col]
    elif matrix[wanted_row][wanted_col] == "C":
        submarine_position = [wanted_row, wanted_col]
        matrix[wanted_row][wanted_col] = "-"
        battle_cruisers_destroyed += 1
        if battle_cruisers_destroyed == 3:
            print("Mission accomplished, U-9 has destroyed all battle cruisers of the enemy!")
            matrix[wanted_row][wanted_col] = "S"
            break
    elif matrix[wanted_row][wanted_col] == "*":
        submarine_position = [wanted_row, wanted_col]
        matrix[wanted_row][wanted_col] = "-"
        mines_hit += 1
        if mines_hit == 3:
            print(f"Mission failed, U-9 disappeared! Last known coordinates [{wanted_row}, {wanted_col}]!")
            matrix[wanted_row][wanted_col] = "S"
            break

for row in matrix:
    print(''.join(row))

# Variant 2
# n = int(input())
#
# directions = {
#     "up": (-1, 0),
#     "down": (1, 0),
#     "left": (0, -1),
#     "right": (0, 1),
# }
#
# matrix = []
# # *--*-
# # -S-*C
# # -*---
# # -----
# # -C-*C
#
# mine_hits = 0
# battle_ships_destroyed = 0
# total_battleships = 3
#
# my_position = []
#
# for row in range(n):
#     matrix.append([x for x in input()])
#
#     if "S" in matrix[row]:
#         my_position = [row, matrix[row].index("S")]
#         matrix[row][my_position[1]] = "-"
#
# while True:
#     direction = input()
#
#     wanted_row = my_position[0] + directions[direction][0]
#     wanted_col = my_position[1] + directions[direction][1]
#
#     if matrix[wanted_row][wanted_col] == "C":
#         matrix[wanted_row][wanted_col] = "-"
#         battle_ships_destroyed += 1
#         if battle_ships_destroyed == 3:
#             matrix[wanted_row][wanted_col] = "S"
#             print(f"Mission accomplished, U-9 has destroyed all battle cruisers of the enemy!")
#             break
#     elif matrix[wanted_row][wanted_col] == "*":
#         matrix[wanted_row][wanted_col] = "-"
#         mine_hits += 1
#         if mine_hits == 3:
#             matrix[wanted_row][wanted_col] = "S"
#             print(f"Mission failed, U-9 disappeared! Last known coordinates [{wanted_row}, {wanted_col}]!")
#             break
#
#     my_position = [wanted_row, wanted_col]
#
# for row in matrix:
#     print(''.join(row))
