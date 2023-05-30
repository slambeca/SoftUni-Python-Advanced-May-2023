SIZE = int(input())
racing_number = input()

directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1),
}

matrix = []
# . . . . .
# . . . T .
# . . . . .
# . T . . .
# . . F . .

distance_covered = 0

car_position = [0, 0]
tunnel_locations = []    # [[1, 3], [3, 1]]

for row in range(SIZE):
    matrix.append(input().split())

    if "T" in matrix[row]:
        tunnel_locations.append([row, matrix[row].index("T")])

while True:
    direction = input()

    if direction == "End":
        print(f"Racing car {racing_number} DNF.")
        matrix[car_position[0]][car_position[1]] = "C"
        break

    wanted_row = car_position[0] + directions[direction][0]
    wanted_col = car_position[1] + directions[direction][1]

    car_position = [wanted_row, wanted_col]

    if matrix[wanted_row][wanted_col] == "T":
        if tunnel_locations[0] == car_position:
            car_position = tunnel_locations[1]
            matrix[wanted_row][wanted_col] = "."
            matrix[car_position[0]][car_position[1]] = "."
        elif tunnel_locations[1] == car_position:
            car_position = tunnel_locations[0]
            matrix[wanted_row][wanted_col] = "."
            matrix[car_position[0]][car_position[1]] = "."
        distance_covered += 30
    elif matrix[wanted_row][wanted_col] == "F":
        print(f"Racing car {racing_number} finished the stage!")
        matrix[wanted_row][wanted_col] = "C"
        distance_covered += 10
        break
    else:
        distance_covered += 10

print(f"Distance covered {distance_covered} km.")
for row in matrix:
    print(''.join(row))