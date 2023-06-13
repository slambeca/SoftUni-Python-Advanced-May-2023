def check_for_indices(r, c, rows, columns):
    if 0 <= r < rows and 0 <= c < columns:
        return True

    return False


rows, columns = [int(x) for x in input().split()]

directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1),
}

matrix = []
# - - - O - P - O
# - P - O O - - -
# - - - - - - O -
# - P B - O - - O
# - - - O - - - -

player_position = []
touched_opponents = 0
moves_made = 0

for row in range(rows):
    matrix.append(input().split())

    if "B" in matrix[row]:
        player_position = [row, matrix[row].index("B")]
        matrix[row][player_position[1]] = "-"

while True:
    direction = input()

    if direction == "Finish":
        break

    wanted_row = player_position[0] + directions[direction][0]
    wanted_col = player_position[1] + directions[direction][1]

    if check_for_indices(wanted_row, wanted_col, rows, columns):
        if matrix[wanted_row][wanted_col] == "O":
            continue
        elif matrix[wanted_row][wanted_col] == "-":
            moves_made += 1
            player_position = [wanted_row, wanted_col]
        elif matrix[wanted_row][wanted_col] == "P":
            touched_opponents += 1
            moves_made += 1
            matrix[wanted_row][wanted_col] = "-"
            player_position = [wanted_row, wanted_col]
            if touched_opponents == 3:
                break

print("Game over!")
print(f"Touched opponents: {touched_opponents} Moves made: {moves_made}")

# Variant 2
# def check_for_indices(r, c, rows, cols):
#     if 0 <= r < rows and 0 <= c < cols:
#         return True
# 
#     return False
# 
# 
# n, m = [int(x) for x in input().split()]
# 
# directions = {
#     "up": (-1, 0),
#     "down": (1, 0),
#     "left": (0, -1),
#     "right": (0, 1),
# }
# 
# my_position = []
# 
# moves_made = 0
# touched_players = 0
# GOAL = 3
# 
# matrix = []
# # - - - O - P - O
# # - P - O O - - -
# # - - - - - - O -
# # - P B - O - - O
# # - - - O - - - -
# 
# for row in range(n):
#     matrix.append(input().split())
# 
#     if "B" in matrix[row]:
#         my_position = [row, matrix[row].index("B")]
#         matrix[row][my_position[1]] = "-"
# 
# while True:
#     direction = input()
# 
#     if direction == "Finish":
#         break
# 
#     wanted_row = my_position[0] + directions[direction][0]
#     wanted_col = my_position[1] + directions[direction][1]
# 
#     if not check_for_indices(wanted_row, wanted_col, n, m) or matrix[wanted_row][wanted_col] == "O":
#         continue
# 
#     moves_made += 1
# 
#     if matrix[wanted_row][wanted_col] == "P":
#         touched_players += 1
#         matrix[wanted_row][wanted_col] = "-"
#         if touched_players == GOAL:
#             break
# 
#     my_position = [wanted_row, wanted_col]
# 
# print(f"Game over!\nTouched opponents: {touched_players} Moves made: {moves_made}")
