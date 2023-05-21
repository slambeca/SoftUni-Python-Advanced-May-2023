def check_indices(r, c, n):
    if 0 <= r < n and 0 <= c < n:
        return True

    return False


collected_hazelnuts = 0

game_won = False
stepped_on_trap = False
out_of_boundaries = False

matrix = []

directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1),
}

n = int(input())
commands = input().split(", ")

squirrel_position = []

for _ in range(n):
    matrix.append(list(input()))

for row in range(n):
    for col in range(n):
        if matrix[row][col] == "s":
            squirrel_position = [row, matrix[row].index("s")]

for direction in commands:
    wanted_row, wanted_col = squirrel_position[0] + directions[direction][0], \
                                 squirrel_position[1] + directions[direction][1]

    if not check_indices(wanted_row, wanted_col, n):
        print("The squirrel is out of the field.")
        out_of_boundaries = True
        break

    if matrix[wanted_row][wanted_col] == "h":
        collected_hazelnuts += 1
        matrix[wanted_row][wanted_col] = "*"
        if collected_hazelnuts == 3:
            print("Good job! You have collected all hazelnuts!")
            game_won = True
            break
    elif matrix[wanted_row][wanted_col] == "t":
        print("Unfortunately, the squirrel stepped on a trap...")
        stepped_on_trap = True
        break

    squirrel_position = [wanted_row, wanted_col]

if not game_won and not stepped_on_trap and not out_of_boundaries:
    print("There are more hazelnuts to collect.")
print(f"Hazelnuts collected: {collected_hazelnuts}")