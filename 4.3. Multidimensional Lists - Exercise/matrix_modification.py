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