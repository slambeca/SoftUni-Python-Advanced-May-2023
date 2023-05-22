def move(direction, steps):
    r = my_position[0] + (directions[direction][0] * steps)
    c = my_position[1] + (directions[direction][1] * steps)

    if not (0 <= r < size and 0 <= c < size):
        return my_position
    if field[r][c] == "x":
        return my_position

    return [r, c]


def shoot(direction):
    r = my_position[0] + directions[direction][0]
    c = my_position[1] + directions[direction][1]

    while 0 <= r < size and 0 <= c < size:
        if field[r][c] == "x":
            field[r][c] = "."
            return [r, c]

        r += directions[direction][0]
        c += directions[direction][1]


size = 5
field = []

targets = 0
targets_hit = 0

targets_hit_positions = []
my_position = []

directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1),
}

for row in range(size):
    field.append(input().split())

    if "A" in field[row]:
        my_position = [row, field[row].index("A")]
        field[row][my_position[1]] = "."

    if "x" in field[row]:
        targets += field[row].count("x")

for _ in range(int(input())):
    command_info = input().split()

    if command_info[0] == "move":
        my_position = move(command_info[1], int(command_info[2]))
    elif command_info[0] == "shoot":
        target_down_pos = shoot(command_info[1])

        if target_down_pos:
            targets_hit_positions.append(target_down_pos)
            targets_hit += 1

        if targets == targets_hit:
            print(f"Training completed! All {targets} targets hit.")
            break
else:
    print(f"Training not completed! {targets - targets_hit} targets left.")

print(*targets_hit_positions, sep="\n")

# Variant 2


# def check_indices(r, c, n):
#     if 0 <= r < n and 0 <= c < n:
#         return True
# 
#     return False
# 
# 
# SIZE = 5
# 
# matrix = []
# # . . . . .
# # x . . . .
# # . A . . .
# # . . . x .
# # . x . . x
# 
# directions = {
#     "up": (-1, 0),
#     "down": (1, 0),
#     "left": (0, -1),
#     "right": (0, 1),
# }
# 
# shooter_position = []    # [2, 1]
# targets_hit_positions = []
# 
# all_targets = 0
# targets_hit = 0
# 
# for row in range(SIZE):
#     matrix.append(input().split())
# 
#     if "A" in matrix[row]:
#         shooter_position = [row, matrix[row].index("A")]  # This is the starting shooters position
#         matrix[row][shooter_position[1]] = "."  # We clear his position
# 
#     if "x" in matrix[row]:
#         all_targets += matrix[row].count("x")  # We find how many targets are there in the field
# 
# number_of_commands = int(input())
# 
# for _ in range(number_of_commands):
#     command = input().split()
# 
#     type_of_command = command[0]
#     direction = command[1]
# 
#     if type_of_command == "shoot":    # shoot down
#         wanted_row = shooter_position[0] + directions[direction][0]
#         wanted_col = shooter_position[1] + directions[direction][1]
# 
#         while check_indices(wanted_row, wanted_col, SIZE):
#             if matrix[wanted_row][wanted_col] == "x":
#                 matrix[wanted_row][wanted_col] = "."
#                 targets_hit += 1
#                 targets_hit_positions.append([wanted_row, wanted_col])
#                 break
# 
#             wanted_row += directions[direction][0]
#             wanted_col += directions[direction][1]
# 
#         if targets_hit == all_targets:
#             print(f"Training completed! All {all_targets} targets hit.")
#             break
# 
#     elif type_of_command == "move":    # move right 4
#         number_of_steps = int(command[2])
#         wanted_row = shooter_position[0] + (directions[direction][0] * number_of_steps)
#         wanted_col = shooter_position[1] + (directions[direction][1] * number_of_steps)
# 
#         if not check_indices(wanted_row, wanted_col, SIZE):    # Do not move the shooter if the index is invalid
#             continue
#         else:
#             if matrix[wanted_row][wanted_col] == ".":
#                 shooter_position = [wanted_row, wanted_col]
# 
# else:
#     print(f"Training not completed! {all_targets - targets_hit} targets left.")
# 
# for row, column in targets_hit_positions:
#     print(f"[{row}, {column}]")
