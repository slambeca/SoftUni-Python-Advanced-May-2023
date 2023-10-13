def check_indices(r, c, row, col):
    if 0 <= r < row and 0 <= c < col:
        return True

    return False


rows, cols = [int(x) for x in input().split(" ")]

directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1),
}

matrix = []
# *----A
# *B***-
# *-***-
# *----P
# ******

starting_position = []
my_position = []

for row in range(rows):
    matrix.append([x for x in input()])

    if "B" in matrix[row]:
        starting_position = [row, matrix[row].index("B")]
        my_position = [row, matrix[row].index("B")]

while True:
    direction = input()

    wanted_row = my_position[0] + directions[direction][0]
    wanted_col = my_position[1] + directions[direction][1]

    if not check_indices(wanted_row, wanted_col, rows, cols):
        print("The delivery is late. Order is canceled.")
        matrix[starting_position[0]][starting_position[1]] = " "
        break

    if matrix[wanted_row][wanted_col] == "*":
        continue

    elif matrix[wanted_row][wanted_col] == "-":
        matrix[wanted_row][wanted_col] = "."

    elif matrix[wanted_row][wanted_col] == "P":
        matrix[wanted_row][wanted_col] = "R"
        print("Pizza is collected. 10 minutes for delivery.")

    elif matrix[wanted_row][wanted_col] == "A":
        matrix[wanted_row][wanted_col] = "P"
        print("Pizza is delivered on time! Next order...")
        break

    my_position = [wanted_row, wanted_col]

for row in matrix:
    print(''.join(row))