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

# Variant 2


# def check_indices(r, c, n):
#     if 0 <= r < n and 0 <= c < n:
#         return True
#
#     return False
#
#
# n = int(input())
#
# collected_teabags = 0
#
# matrix = []
#
# for _ in range(n):
#     matrix.append(input().split())
# # . A . . 1
# # R . 2 . .
# # 4 7 . 1 .
# # . . . 2 .
# # . 3 . . .
#
# alice_position = []
#
# directions = {
#     "up": (-1, 0),
#     "down": (1, 0),
#     "left": (0, -1),
#     "right": (0, 1),
# }
#
# for row in range(n):
#     for col in range(n):
#         if matrix[row][col] == "A":
#             alice_position = [row, matrix[row].index("A")]
#             matrix[row][col] = "*"
#
# while True:
#     command = input()    # down
#
#     wanted_row, wanted_col = alice_position[0] + directions[command][0], alice_position[1] + directions[command][1]
#
#     if not check_indices(wanted_row, wanted_col, n):
#         print("Alice didn't make it to the tea party.")
#         break
#     else:
#         if matrix[wanted_row][wanted_col] == "R":
#             print(f"Alice didn't make it to the tea party.")
#             matrix[wanted_row][wanted_col] = "*"
#             break
#         elif matrix[wanted_row][wanted_col].isdigit():
#             collected_teabags += int(matrix[wanted_row][wanted_col])
#             matrix[wanted_row][wanted_col] = "*"
#             if collected_teabags >= 10:
#                 print(f"She did it! She went to the party.")
#                 break
#         elif matrix[wanted_row][wanted_col] == ".":
#             matrix[wanted_row][wanted_col] = "*"
#
#         alice_position = [wanted_row, wanted_col]
#
# [print(*row) for row in matrix]

# Variant 3
# def check_indices(r, c, n):
#     if 0 <= r < n and 0 <= c < n:
#         return True
#
#     return False
#
#
# SIZE = int(input())
#
# directions = {
#     "up": (-1, 0),
#     "down": (1, 0),
#     "left": (0, -1),
#     "right": (0, 1),
# }
#
# matrix = []
#
# alice_position = []
#
# collected_bags_of_tea = 0
#
# for row in range(SIZE):
#     matrix.append(input().split())
#
#     if "A" in matrix[row]:
#         alice_position = [row, matrix[row].index("A")]
#
#         matrix[alice_position[0]][alice_position[1]] = "*"
#
# # . A . . 1
# # R . 2 . .
# # 4 7 . 1 .
# # . . . 2 .
# # . 3 . . .
#
# while True:
#     direction = input()
#
#     wanted_row = alice_position[0] + directions[direction][0]
#     wanted_col = alice_position[1] + directions[direction][1]
#
#     if not check_indices(wanted_row, wanted_col, SIZE):
#         print(f"Alice didn't make it to the tea party.")
#         break
#     else:
#         if matrix[wanted_row][wanted_col].isdigit():
#             collected_bags_of_tea += int(matrix[wanted_row][wanted_col])
#             matrix[wanted_row][wanted_col] = "*"
#             if collected_bags_of_tea >= 10:
#                 print("She did it! She went to the party.")
#                 break
#         elif matrix[wanted_row][wanted_col] == "R":
#             matrix[wanted_row][wanted_col] = "*"
#             print(f"Alice didn't make it to the tea party.")
#             break
#
#     alice_position = [wanted_row, wanted_col]
#     matrix[wanted_row][wanted_col] = "*"
#
# [print(*row) for row in matrix]
