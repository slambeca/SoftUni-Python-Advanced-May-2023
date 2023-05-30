def check_for_indices(r, c, some_array):
    if 0 <= r < some_array and 0 <= c < some_array:
        return True

    return False


string = input()
size = int(input())

directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1),
}

matrix = []
# P---
# Mark
# -l-y
# --e-

player_position = []    # [0, 0]

for row in range(size):
    matrix.append([x for x in input()])

    if "P" in matrix[row]:
        player_position = [row, matrix[row].index("P")]
        matrix[row][player_position[1]] = "-"

for _ in range(int(input())):
    direction = input()    # down

    wanted_row = player_position[0] + directions[direction][0]
    wanted_col = player_position[1] + directions[direction][1]

    if check_for_indices(wanted_row, wanted_col, size):
        if matrix[wanted_row][wanted_col] != "-":
            string += matrix[wanted_row][wanted_col]
            matrix[wanted_row][wanted_col] = "-"
            player_position = [wanted_row, wanted_col]
        else:
            player_position = [wanted_row, wanted_col]
    else:
        if string:
            string = string[:-1]

matrix[player_position[0]][player_position[1]] = "P"

print(string)
for row in matrix:
    print(''.join(row))