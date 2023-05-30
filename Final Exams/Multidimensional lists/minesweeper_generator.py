def check_indices(r, c, some_array):
    if 0 <= r < some_array and 0 <= c < some_array:
        return True

    return False


n = int(input())
bombs = int(input())

directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1),
    "up-left": (-1, -1),
    "up-right": (-1, 1),
    "down-left": (1, -1),
    "down-right": (1, 1),
}

matrix = []
# 0 0 0 *
# 0 * 0 0
# 0 0 * 0
# * 0 0 0

for row in range(n):
    matrix.append([])
    for col in range(n):
        matrix[row].append(0)

for _ in range(bombs):
    coordinates = input().split(", ")

    wanted_row = int(coordinates[0].strip("("))
    wanted_col = int(coordinates[1].strip(")"))

    matrix[wanted_row][wanted_col] = "*"

for current_row in range(n):
    for current_col in range(n):
        if matrix[current_row][current_col] != "*":
            for direction in directions:
                new_wanted_row = current_row + directions[direction][0]
                new_wanted_col = current_col + directions[direction][1]
                if check_indices(new_wanted_row, new_wanted_col, n):
                    if matrix[new_wanted_row][new_wanted_col] == "*":
                        matrix[current_row][current_col] += 1

[print(*row) for row in matrix]