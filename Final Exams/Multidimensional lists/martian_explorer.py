SIZE = 6

matrix = []
# - R - - - -
# - - - - - R
# - E - R - -
# - W - - - -
# - - - C - -
# M - - - - -

rover_position = []    # [2, 1]

water_collected = 0
metal_collected = 0
concrete_collected = 0

directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1),
}

for row in range(SIZE):
    matrix.append(input().split())

    if "E" in matrix[row]:
        rover_position = [row, matrix[row].index("E")]
        matrix[row][rover_position[1]] = "-"

commands = input().split(", ")    # ['down', 'right', 'down', 'right', 'down', 'left', 'left', 'left']

for direction in commands:
    wanted_row = rover_position[0] + directions[direction][0]    # 3
    wanted_col = rover_position[1] + directions[direction][1]    # 1

    if wanted_row < 0:
        wanted_row = SIZE - 1
    elif wanted_row == SIZE:
        wanted_row = 0

    if wanted_col < 0:
        wanted_col = SIZE - 1
    elif wanted_col == SIZE:
        wanted_col = 0

    current_position = matrix[wanted_row][wanted_col]

    if current_position == "W":
        matrix[wanted_row][wanted_col] = "-"
        water_collected += 1
        print(f"Water deposit found at {wanted_row, wanted_col}")
    elif current_position == "M":
        matrix[wanted_row][wanted_col] = "-"
        metal_collected += 1
        print(f"Metal deposit found at {wanted_row, wanted_col}")
    elif current_position == "C":
        matrix[wanted_row][wanted_col] = "-"
        concrete_collected += 1
        print(f"Concrete deposit found at {wanted_row, wanted_col}")
    elif current_position == "R":
        rover_position = [wanted_row, wanted_col]
        print(f"Rover got broken at {tuple(rover_position)}")
        break

    rover_position = [wanted_row, wanted_col]

if water_collected and metal_collected and concrete_collected:
    print("Area suitable to start the colony.")
else:
    print("Area not suitable to start the colony.")

# Variant 2
# SIZE = 6
#
# mars = []
# rover_pos = []
#
# directions = {
#     "up": lambda r, c: [(r - 1) % SIZE, c],
#     "down": lambda r, c: [(r + 1) % SIZE, c],
#     "left": lambda r, c: [r, (c - 1) % SIZE],
#     "right": lambda r, c: [r, (c + 1) % SIZE],
# }
#
# deposits = {"W": ["Water", 0], "M": ["Metal", 0], "C": ["Concrete", 0]}
#
# for row in range(SIZE):
#     current_row = input().split()
#
#     if "E" in current_row:
#         rover_pos = [row, current_row.index("E")]
#
#     mars.append(current_row)
#
# commands = input().split(", ")
#
# for command in commands:
#     rover_pos = directions[command](*rover_pos)
#     position = mars[rover_pos[0]][rover_pos[1]]
#
#     if position in deposits:
#         print(f"{deposits[position][0]} deposit found at ({rover_pos[0]}, {rover_pos[1]})")
#
#         deposits[position][1] += 1
#
#     elif position == "R":
#         print(f"Rover got broken at ({rover_pos[0]}, {rover_pos[1]})")
#         break
#
# if all([deposits["W"][1], deposits["M"][1], deposits["C"][1]]):
#     print("Area suitable to start the colony.")
# else:
#     print("Area not suitable to start the colony.")
