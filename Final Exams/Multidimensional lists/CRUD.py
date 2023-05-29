SIZE = 6

directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1),
}

matrix = []    # letters, numbers and empty positions
# . . . . . .
# . 6 . . . .
# G . S . t S
# . . 10 . . .
# . 95 . . 8 .
# . . P . . .

for row in range(SIZE):
    matrix.append(input().split())

starting_position = input().split(", ")    # # ['(1', '1)']
starting_row = int(starting_position[0].strip("("))
starting_col = int(starting_position[1].strip(")"))

my_position = [starting_row, starting_col]

while True:
    command = input()

    if command == "Stop":
        break

    command_args = command.split(", ")

    type_of_command = command_args[0]
    direction = command_args[1]

    wanted_row = my_position[0] + directions[direction][0]
    wanted_col = my_position[1] + directions[direction][1]

    if type_of_command == "Create":
        value = command_args[2]
        if matrix[wanted_row][wanted_col] == ".":
            matrix[wanted_row][wanted_col] = value

    elif type_of_command == "Update":
        value = command_args[2]
        if matrix[wanted_row][wanted_col] != ".":
            matrix[wanted_row][wanted_col] = value

    elif type_of_command == "Read":
        if matrix[wanted_row][wanted_col] != ".":
            print(matrix[wanted_row][wanted_col])

    elif type_of_command == "Delete":
        if matrix[wanted_row][wanted_col] != ".":
            matrix[wanted_row][wanted_col] = "."

    my_position = [wanted_row, wanted_col]

[print(*row) for row in matrix]