n = int(input())

commands = input().split()

matrix = []
miner_position = []
collected_coal, total_coal = 0, 0

directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1),
}

for row in range(n):
    matrix.append(input().split())

    if "s" in matrix[row]:
        miner_position = [row, matrix[row].index("s")]
        matrix[row][miner_position[1]] = "*"

    total_coal += matrix[row].count("c")

for command in commands:
    r, c = miner_position[0] + directions[command][0], miner_position[1] + directions[command][1]

    if not (0 <= r < n and 0 <= c < n):
        continue

    miner_position = [r, c]

    if matrix[r][c] == "c":
        collected_coal += 1

        if collected_coal == total_coal:
            print(f"You collected all coal! ({r}, {c})")
            break

    elif matrix[r][c] == "e":
        print(f"Game over! ({r}, {c})")
        break

    matrix[r][c] = "*"
else:
    print(f"{total_coal - collected_coal} pieces of coal left. ({miner_position[0]}, {miner_position[1]})")

# Variant 2


# def check_indices(row, col):
#     if 0 <= row < rows and 0 <= col < rows:
#         return True
#
#     return False
#
#
# rows = int(input())    # 5
#
# commands = [x for x in input().split()]    # ['up', 'right', 'right', 'up', 'right']
#
# matrix = []
# miner_position = []
#
# collected_coal = 0
# total_coal = 0    # 4
#
# # * * * c *
# # * * * e *
# # * * c * *
# # s * * c *
# # * * c * *
#
# directions = {
#     "left": (0, -1),
#     "right": (0, 1),
#     "up": (-1, 0),
#     "down": (1, 0),
# }
#
# for row in range(rows):
#     current_row = input().split()
#     matrix.append(current_row)
#
#     if "s" in matrix[row]:
#         miner_position = [row, matrix[row].index("s")]    # [3, 0]
#         matrix[row][miner_position[1]] = "*"    # We replace the "s" with "*"
#
#     total_coal += matrix[row].count("c")
#
# for command in commands:    # up
#     wanted_row, wanted_col = miner_position[0] + directions[command][0], miner_position[1] + directions[command][1]
#     # we are not yet moving the miner, we first have to check if the indexes are valid
#
#     if check_indices(wanted_row, wanted_col):
#         miner_position = wanted_row, wanted_col
#
#         if matrix[wanted_row][wanted_col] == "c":
#             collected_coal += 1
#             matrix[wanted_row][wanted_col] = "*"
#
#             if collected_coal == total_coal:
#                 print(f"You collected all coal! ({wanted_row}, {wanted_col})")
#                 raise SystemExit
#         elif matrix[wanted_row][wanted_col] == "e":
#             print(f"Game over! ({wanted_row}, {wanted_col})")
#             raise SystemExit
#     else:
#         continue
# else:
#     print(f"{total_coal - collected_coal} pieces of coal left. ({miner_position[0]}, {miner_position[1]})")

# Variant 3
# def check_indices(r, c, n):
#     if 0 <= r < n and 0 <= c < n:
#         return True
# 
#     return False
# 
# 
# SIZE = int(input())
# 
# commands = input().split()    # ['up', 'right', 'right', 'up', 'right']
# 
# miner_position = []
# 
# collected_coal = 0
# total_coal = 0
# 
# matrix = []
# # * * * c *
# # * * * e *
# # * * c * *
# # s * * c *
# # * * c * *
# 
# directions = {
#     "up": (-1, 0),
#     "down": (1, 0),
#     "left": (0, -1),
#     "right": (0, 1),
# }
# 
# for row in range(SIZE):
#     matrix.append(input().split())
# 
#     if "s" in matrix[row]:
#         miner_position = [row, matrix[row].index("s")]
#         matrix[miner_position[0]][miner_position[1]] = "*"
# 
#     total_coal += matrix[row].count("c")
# 
# for direction in commands:
#     wanted_row = miner_position[0] + directions[direction][0]
#     wanted_col = miner_position[1] + directions[direction][1]
# 
#     if not check_indices(wanted_row, wanted_col, SIZE):
#         continue
# 
#     if matrix[wanted_row][wanted_col] == "e":
#         print(f"Game over! ({wanted_row}, {wanted_col})")
#         break
#     elif matrix[wanted_row][wanted_col] == "c":
#         matrix[wanted_row][wanted_col] = "*"
#         collected_coal += 1
#         if collected_coal == total_coal:
#             print(f"You collected all coal! ({wanted_row}, {wanted_col})")
#             break
# 
#     miner_position = [wanted_row, wanted_col]
# else:
#     print(f"{total_coal - collected_coal} pieces of coal left. ({miner_position[0]}, {miner_position[1]})")
