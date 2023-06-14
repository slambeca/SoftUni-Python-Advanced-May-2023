data = [int(x) for x in input().split(", ")]
rows, cols = data[0], data[1]

my_position = []

items_collected = False

directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1),
}

all_items = 0
christmas_decorations, gifts, cookies = 0, 0, 0

matrix = []
# . . . . .
# C . . G .
# . C . . .
# G . . C .
# . D . . D
# Y . . . G

for row in range(rows):
    matrix.append(input().split())

    if "Y" in matrix[row]:
        my_position = [row, matrix[row].index("Y")]
        matrix[row][my_position[1]] = "x"
    if "D" in matrix[row]:
        all_items += matrix[row].count("D")
    if "C" in matrix[row]:
        all_items += matrix[row].count("C")
    if "G" in matrix[row]:
        all_items += matrix[row].count("G")

while True:
    command = input()

    if command == "End":
        break

    command_args = command.split("-")

    direction = command_args[0]
    steps = int(command_args[1])

    for step in range(steps):
        wanted_row = my_position[0] + directions[direction][0]
        wanted_col = my_position[1] + directions[direction][1]

        if wanted_row == -1:
            wanted_row = rows - 1
        elif wanted_row >= rows:
            wanted_row = 0

        if wanted_col == -1:
            wanted_col = cols - 1
        elif wanted_col >= cols:
            wanted_col = 0

        if matrix[wanted_row][wanted_col] == "G":
            gifts += 1
        elif matrix[wanted_row][wanted_col] == "C":
            cookies += 1
        elif matrix[wanted_row][wanted_col] == "D":
            christmas_decorations += 1

        matrix[wanted_row][wanted_col] = "x"

        my_position = [wanted_row, wanted_col]

        if gifts + christmas_decorations + cookies == all_items:
            items_collected = True
            print("Merry Christmas!")
            break

    if items_collected:
        break

matrix[my_position[0]][my_position[1]] = "Y"

print(f"You've collected:\n- {christmas_decorations} Christmas decorations\n- {gifts} Gifts\n- {cookies} Cookies")
[print(*row) for row in matrix]