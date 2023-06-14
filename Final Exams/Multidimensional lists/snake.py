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
   
# Variant 2 
# def check_for_indices(r, c, some_array):
#     if 0 <= r < some_array and 0 <= c < some_array:
#         return True
# 
#     return False
# 
# 
# n = int(input())
# 
# directions = {
#     "up": (-1, 0),
#     "down": (1, 0),
#     "left": (0, -1),
#     "right": (0, 1),
# }
# 
# food_eaten = 0
# GOAL = 10
# 
# matrix = []
# # -----S
# # ----B-
# # ------
# # ------
# # --B---
# # --*---
# 
# my_position = []
# burrows_positions = []    # [[0, 4], [4, 2]]
# stepped_on_burrow = False
# 
# for row in range(n):
#     matrix.append([x for x in input()])
# 
#     if "S" in matrix[row]:
#         my_position = [row, matrix[row].index("S")]
#         matrix[row][my_position[1]] = "."
#     if "B" in matrix[row]:
#         burrows_positions.append([row, matrix[row].index("B")])
# 
# while True:
#     direction = input()
# 
#     wanted_row = my_position[0] + directions[direction][0]
#     wanted_col = my_position[1] + directions[direction][1]
# 
#     if not check_for_indices(wanted_row, wanted_col, n):
#         print("Game over!")
#         break
# 
#     if matrix[wanted_row][wanted_col] == "*":
#         matrix[wanted_row][wanted_col] = "."
#         food_eaten += 1
#         if food_eaten == GOAL:
#             matrix[wanted_row][wanted_col] = "S"
#             print("You won! You fed the snake.")
#             break
#     elif matrix[wanted_row][wanted_col] == "-":
#         matrix[wanted_row][wanted_col] = "."
#     elif matrix[wanted_row][wanted_col] == "B":
#         stepped_on_burrow = True
#         if [wanted_row, wanted_col] == burrows_positions[0]:
#             wanted_row, wanted_col = burrows_positions[1][0], burrows_positions[1][1]
#         elif [wanted_row, wanted_col] == burrows_positions[1]:
#             wanted_row, wanted_col = burrows_positions[0][0], burrows_positions[0][1]
# 
#     if stepped_on_burrow:
#         stepped_on_burrow = False
#         for position in burrows_positions:
#             matrix[position[0]][position[1]] = "."
# 
#     my_position = [wanted_row, wanted_col]
# 
# print(f"Food eaten: {food_eaten}")
# for row in matrix:
#     print(''.join(row))
