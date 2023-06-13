def check_indices(idx1, idx2, some_array):
    if 0 <= idx1 < len(some_array) and 0 <= idx2 < len(some_array):
        return True

    return False


matrix = [[int(x) for x in input().split()] for _ in range(int(input()))]
# [[1, 2, 3],
# [4, 5, 6],
# [7, 8, 9]]

COMMAND_END = "END"
COMMAND_ADD = "Add"
COMMAND_SUBTRACT = "Subtract"

while True:
    command = input()

    if command == COMMAND_END:
        break

    command_args = command.split()

    type_of_command = command_args[0]    # Add
    row = int(command_args[1])    # 0
    column = int(command_args[2])    # 0
    new_value = int(command_args[3])    # 5

    if not check_indices(row, column, matrix):
        print("Invalid coordinates")
        continue

    if type_of_command == COMMAND_ADD:
        matrix[row][column] += new_value
    elif type_of_command == COMMAND_SUBTRACT:
        matrix[row][column] -= new_value

for row in matrix:
    print(*row)

# Variant 2
# n = int(input())
#
# matrix = [[int(x) for x in input().split()] for _ in range(n)]
#
# command = input().split()
#
# while command[0] != "END":
#     type_command, row, column, num = command[0], int(command[1]), int(command[2]), int(command[3])
#
#     if not (0 <= row < n and 0 <= column < n):
#         print("Invalid coordinates")
#     elif type_command == "Add":
#         matrix[row][column] += num
#     elif type_command == "Subtract":
#         matrix[row][column] -= num
#
#     command = input().split()
#
# [print(*row) for row in matrix]

# Variant 3


# def check_indices(r, c, n):
#     if 0 <= r < n and 0 <= c < n:
#         return True
#
#     return False
#
#
# n = int(input())
#
# matrix = []
#
# for _ in range(n):
#     numbers = [int(x) for x in input().split()]
#
#     matrix.append(numbers)
#
# COMMAND_END = "END"
# COMMAND_ADD = "Add"
# COMMAND_SUBTRACT = "Subtract"
#
# # 1 2 3
# # 4 5 6
# # 7 8 9
#
# while True:
#     command = input()
#
#     if command == COMMAND_END:
#         break
#
#     command_args = command.split()
#
#     type_of_command = command_args[0]
#     row = int(command_args[1])
#     col = int(command_args[2])
#     new_value = int(command_args[3])
#
#     if check_indices(row, col, n):
#         if type_of_command == COMMAND_ADD:
#             matrix[row][col] += new_value
#         elif type_of_command == COMMAND_SUBTRACT:
#             matrix[row][col] -= new_value
#     else:
#         print("Invalid coordinates")
#
# [print(*row) for row in matrix]

# Variant 4
# def check_indices(r, c, n):
#     if 0 <= r < n and 0 <= c < n:
#         return True
# 
#     return False
# 
# 
# SIZE = int(input())
# 
# matrix = []
# # 1 2 3
# # 4 5 6
# # 7 8 9
# 
# for row in range(SIZE):
#     matrix.append([int(x) for x in input().split()])
# 
# while True:
#     command = input()
# 
#     if command == "END":
#         break
# 
#     command_args = command.split()
# 
#     type_of_action = command_args[0]
#     row, col, value = int(command_args[1]), int(command_args[2]), int(command_args[3])
# 
#     if type_of_action == "Add":
#         if check_indices(row, col, SIZE):
#             matrix[row][col] += value
#         else:
#             print("Invalid coordinates")
#     elif type_of_action == "Subtract":
#         if check_indices(row, col, SIZE):
#             matrix[row][col] -= value
#         else:
#             print("Invalid coordinates")
# 
# [print(*row) for row in matrix]
