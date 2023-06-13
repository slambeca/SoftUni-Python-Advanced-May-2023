def check_indices(r, c, size):
    if 0 <= r < size and 0 <= c < size:
        return True

    return False


n = int(input())

directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1),
}

matrix = []
# . . p .
# . . . .
# . . t .
# t . . .

plane_position = []    # [0, 2]
all_targets = 0
killed_targets = 0
game_won = False

for row in range(n):
    matrix.append(input().split())

    if "p" in matrix[row]:
        plane_position = [row, matrix[row].index("p")]    # With one object, we use index
        matrix[row][plane_position[1]] = "."
    if "t" in matrix[row]:
        all_targets += matrix[row].count("t")    # With multiple objects, we use count

m = int(input())

for _ in range(m):
    command = input().split()

    action, direction, steps = command[0], command[1], int(command[2])

    wanted_row = plane_position[0] + directions[direction][0] * steps
    wanted_col = plane_position[1] + directions[direction][1] * steps

    if action == "shoot":
        if check_indices(wanted_row, wanted_col, n):
            if matrix[wanted_row][wanted_col] == "t":
                matrix[wanted_row][wanted_col] = "x"
                killed_targets += 1
                if killed_targets == all_targets:
                    game_won = True
                    break
            else:
                matrix[wanted_row][wanted_col] = "x"
    elif action == "move":
        if check_indices(wanted_row, wanted_col, n):
            if matrix[wanted_row][wanted_col] == "." and matrix[wanted_row][wanted_col] != "x":
                matrix[plane_position[0]][plane_position[1]] = "."
                matrix[wanted_row][wanted_col] = "p"
                plane_position = [wanted_row, wanted_col]

if game_won:
    print(f"Mission accomplished! All {all_targets} targets destroyed.")
else:
    print(f"Mission failed! {all_targets - killed_targets} targets left.")
[print(*row) for row in matrix]

# Variant 2
# def check_for_indices(r, c, some_array):
#     if 0 <= r < some_array and 0 <= c < some_array:
#         return True
#
#     return False
#
#
# n = int(input())
#
# killed_targets = 0
# all_targets = 0
#
# my_position = []
#
# matrix = []
# # . . p .
# # . . . .
# # . . t .
# # t . . .
#
# directions = {
#     "up": (-1, 0),
#     "down": (1, 0),
#     "left": (0, -1),
#     "right": (0, 1),
# }
#
# for row in range(n):
#     matrix.append(input().split())
#
#     if "p" in matrix[row]:
#         my_position = [row, matrix[row].index("p")]
#         matrix[row][my_position[1]] = "."
#     if "t" in matrix[row]:
#         all_targets += matrix[row].count("t")
#
# m = int(input())
#
# for _ in range(m):
#     command = input().split()
#
#     type_of_command = command[0]
#     direction = command[1]
#     steps = int(command[2])
#
#     if type_of_command == "move":
#         wanted_row = my_position[0] + directions[direction][0] * steps
#         wanted_col = my_position[1] + directions[direction][1] * steps
#         if check_for_indices(wanted_row, wanted_col, n):
#             if matrix[wanted_row][wanted_col] == ".":
#                 matrix[wanted_row][wanted_col] = "p"
#                 matrix[my_position[0]][my_position[1]] = "."
#                 my_position = [wanted_row, wanted_col]
#
#     elif type_of_command == "shoot":
#         wanted_row = my_position[0] + directions[direction][0] * steps
#         wanted_col = my_position[1] + directions[direction][1] * steps
#         if check_for_indices(wanted_row, wanted_col, n):
#             if matrix[wanted_row][wanted_col] == "t":
#                 matrix[wanted_row][wanted_col] = "x"
#                 killed_targets += 1
#                 if killed_targets == all_targets:
#                     print(f"Mission accomplished! All {all_targets} targets destroyed.")
#                     break
#             else:
#                 matrix[wanted_row][wanted_col] = "x"
# else:
#     print(f"Mission failed! {all_targets - killed_targets} targets left.")
#
# [print(*row) for row in matrix]
