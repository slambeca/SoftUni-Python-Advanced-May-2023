n = int(input())

matrix = []
# [['1', '3', '7', '9', '11'],
# ['X', '5', '4', 'X', '63'],
# ['7', '3', '21', '95', '1'],
# ['B', '1', '73', '4', '9'],
# ['9', '2', '33', '2', '0']]

bunny_pos = []
best_path = []

best_direction = None
max_collected_eggs = 0

directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1),
}

for row in range(n):
    matrix.append(input().split())
    if "B" in matrix[row]:
        bunny_pos = [row, matrix[row].index("B")]

for direction, positions in directions.items():
    row, col = [
        bunny_pos[0] + positions[0], bunny_pos[1] + positions[1]
    ]

    path = []
    collected_eggs = 0

    while 0 <= row < n and 0 <= col < n:
        if matrix[row][col] == "X":
            break

        collected_eggs += int(matrix[row][col])
        path.append([row, col])

        row += positions[0]
        col += positions[1]

    if collected_eggs >= max_collected_eggs:
        max_collected_eggs = collected_eggs
        best_direction = direction
        best_path = path

print(best_direction)
for element in best_path:    # print(*best_path, sep="\n")
    print(element, end="\n")
print(max_collected_eggs)