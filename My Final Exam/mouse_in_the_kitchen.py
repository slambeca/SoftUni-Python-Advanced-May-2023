def check_indices(r, c, row, col):
    if 0 <= r < row and 0 <= c < col:
        return True

    return False


rows, cols = [int(x) for x in input().split(",")]    # 5, 5

directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1),
}

matrix = []
# * * M * *
# T @ @ * *
# C C @ * *
# * * @ @ *
# * * C C *

my_position = []    # [0, 2]
total_cheese = 0
cheese_eaten = 0

for row in range(rows):
    matrix.append([x for x in input()])

    if "M" in matrix[row]:
        my_position = [row, matrix[row].index("M")]
        matrix[row][my_position[1]] = "*"

    if "C" in matrix[row]:
        total_cheese += matrix[row].count("C")

while True:
    direction = input()

    if direction == "danger":
        print("Mouse will come back later!")
        matrix[my_position[0]][my_position[1]] = "M"
        break

    wanted_row = my_position[0] + directions[direction][0]
    wanted_col = my_position[1] + directions[direction][1]

    if not check_indices(wanted_row, wanted_col, rows, cols):
        matrix[my_position[0]][my_position[1]] = "M"
        print("No more cheese for tonight!")
        break

    if matrix[wanted_row][wanted_col] == "C":
        matrix[wanted_row][wanted_col] = "*"
        cheese_eaten += 1
        if cheese_eaten == total_cheese:
            matrix[wanted_row][wanted_col] = "M"
            print("Happy mouse! All the cheese is eaten, good night!")
            break
    elif matrix[wanted_row][wanted_col] == "@":
        continue
    elif matrix[wanted_row][wanted_col] == "T":
        matrix[wanted_row][wanted_col] = "M"
        print("Mouse is trapped!")
        break

    my_position = [wanted_row, wanted_col]

for row in matrix:
    print(''.join(row))