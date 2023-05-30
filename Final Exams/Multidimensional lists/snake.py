def check_indices(r, c, some_size):
    if 0 <= r < some_size and 0 <= c < some_size:
        return True

    return False


size = int(input())

directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1),
}

matrix = [list(input()) for _ in range(size)]
# - - - - - S
# - - - - B -
# - - - - - -
# - - - - - -
# - - B - - -
# - - * - - -

snake_position = []    # [0, 5]
burrows_positions = []    # [[1, 4], [4, 2]]

food_eaten = 0
NEEDED_FOOD = 10

for row in range(size):
    for col in range(size):
        if matrix[row][col] == "S":
            snake_position = [row, col]
            matrix[row][col] = "."
        if matrix[row][col] == "B":
            burrows_positions.append([row, col])

while True:
    direction = input()    # left

    wanted_row = snake_position[0] + directions[direction][0]    # 0
    wanted_col = snake_position[1] + directions[direction][1]    # 4

    if check_indices(wanted_row, wanted_col, size):
        snake_position = [wanted_row, wanted_col]
        if matrix[wanted_row][wanted_col] == "*":
            food_eaten += 1
            matrix[wanted_row][wanted_col] = "."
            if food_eaten == 10:
                print("You won! You fed the snake.")
                matrix[wanted_row][wanted_col] = "S"
                break
        elif matrix[wanted_row][wanted_col] == "B":
            if burrows_positions[0] == snake_position:
                snake_position = burrows_positions[1]
                matrix[wanted_row][wanted_col] = "."
                matrix[snake_position[0]][snake_position[1]] = "."
            elif burrows_positions[1] == snake_position:
                snake_position = burrows_positions[0]
                matrix[wanted_row][wanted_col] = "."
                matrix[snake_position[0]][snake_position[1]] = "."
        elif matrix[wanted_row][wanted_col] == "-":
            matrix[wanted_row][wanted_col] = "."
    else:
        print("Game over!")
        break

print(f"Food eaten: {food_eaten}")
for row in matrix:
    print(''.join(row))