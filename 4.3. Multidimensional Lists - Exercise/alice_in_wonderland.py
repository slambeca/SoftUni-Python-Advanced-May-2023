n = int(input())

matrix = []
alice_pos = []

tea_bags = 0

directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1),
}

for row in range(n):
    matrix.append(input().split())

    if "A" in matrix[row]:
        alice_pos = [row, matrix[row].index("A")]
        matrix[row][alice_pos[1]] = "*"

while tea_bags < 10:
    direction = input()

    row = alice_pos[0] + directions[direction][0]
    column = alice_pos[1] + directions[direction][1]

    if not (0 <= row < n and 0 <= column < n):
        break

    alice_pos = [row, column]
    position = matrix[row][column]
    matrix[row][column] = "*"

    if position == "R":
        break

    if position.isdigit():
        tea_bags += int(position)

if tea_bags < 10:
    print("Alice didn't make it to the tea party.")
else:
    print("She did it! She went to the party.")

for row in matrix:
    print(*row)