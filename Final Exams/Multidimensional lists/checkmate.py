def check_indices(r, c, n):
    if 0 <= r < n and 0 <= c < n:
        return True

    return False


SIZE = 8

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
queens_coordinates = []

# . . . . . . . .
# Q . . . . . . .
# . K . . . Q . .
# . . . Q . . . .
# Q . . . Q . . .
# . Q . . . . . .
# . . . . . . Q .
# . Q . Q . . . .

queens_successful_coordinates = []

for row in range(SIZE):
    matrix.append(input().split())

for r in range(SIZE):
    for c in range(SIZE):
        if matrix[r][c] == "Q":
            queens_coordinates.append([r, c])

for queen in queens_coordinates:
    for direction in directions:
        wanted_row = queen[0] + directions[direction][0]
        wanted_col = queen[1] + directions[direction][1]
        while check_indices(wanted_row, wanted_col, SIZE):
            if matrix[wanted_row][wanted_col] == "K":
                queens_successful_coordinates.append([queen[0], queen[1]])
                break
            elif matrix[wanted_row][wanted_col] == "Q":
                break

            wanted_row += directions[direction][0]
            wanted_col += directions[direction][1]

if queens_successful_coordinates:
    for current_list in queens_successful_coordinates:
        print(current_list)
else:
    print("The king is safe!")