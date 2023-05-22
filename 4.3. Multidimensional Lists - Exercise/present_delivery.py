def eat_cookie(presents_left, nice_kids):
    for x, y in directions.values():
        r = santa_pos[0] + x
        c = santa_pos[1] + y

        if neighborhood[r][c].isalpha():
            if neighborhood[r][c] == "V":
                nice_kids += 1

            neighborhood[r][c] = "-"
            presents_left -= 1

        if not presents_left:
            break

    return presents_left, nice_kids


presents = int(input())
size = int(input())

neighborhood = []
santa_pos = []

total_nice_kids = 0
nice_kids_visited = 0

directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1),
}

for row in range(size):
    line = input().split()

    neighborhood.append(line)

    if "S" in line:
        santa_pos = [row, line.index("S")]
        neighborhood[row][santa_pos[1]] = "-"    # We clear the position of Santa

    total_nice_kids += line.count("V")

command = input()

while command != "Christmas morning":
    santa_pos = [
        santa_pos[0] + directions[command][0],
        santa_pos[1] + directions[command][1]
    ]

    house = neighborhood[santa_pos[0]][santa_pos[1]]

    if house == "V":
        nice_kids_visited += 1
        presents -= 1
    elif house == "C":
        presents, nice_kids_visited = eat_cookie(presents, nice_kids_visited)

    neighborhood[santa_pos[0]][santa_pos[1]] = "-"

    if not presents or total_nice_kids == nice_kids_visited:
        break

    command = input()

neighborhood[santa_pos[0]][santa_pos[1]] = "S"


if not presents and nice_kids_visited < total_nice_kids:
    print(f"Santa ran out of presents!")

[print(*row) for row in neighborhood]

if nice_kids_visited == total_nice_kids:
    print(f"Good job, Santa! {total_nice_kids} happy nice kid/s.")
else:
    print(f"No presents for {total_nice_kids - nice_kids_visited} nice kid/s.")
    
# Variant 2
# number_of_presents = int(input())
# n = int(input())
# 
# neighborhood = []
# # - X V -
# # - S - V
# # - - - -
# # X - - -
# 
# total_nice_kids = 0
# nice_kids_visited = 0
# 
# directions = {
#     "up": (-1, 0),
#     "down": (1, 0),
#     "left": (0, -1),
#     "right": (0, 1),
# }
# 
# santas_position = []  # [1, 1]
# 
# for row in range(n):
#     neighborhood.append(input().split())
# 
#     if "S" in neighborhood[row]:
#         santas_position = [row, neighborhood[row].index("S")]
#         neighborhood[row][santas_position[1]] = "-"
# 
#     if "V" in neighborhood[row]:
#         total_nice_kids += neighborhood[row].count("V")
# 
# command = input()
# 
# while command != "Christmas morning":
#     wanted_row = santas_position[0] + directions[command][0]
#     wanted_col = santas_position[1] + directions[command][1]
# 
#     if neighborhood[wanted_row][wanted_col] == "X":
#         neighborhood[wanted_row][wanted_col] = "-"
#         santas_position = [wanted_row, wanted_col]
# 
#     elif neighborhood[wanted_row][wanted_col] == "V":
#         neighborhood[wanted_row][wanted_col] = "-"
#         number_of_presents -= 1
#         nice_kids_visited += 1
#         santas_position = [wanted_row, wanted_col]
# 
#     elif neighborhood[wanted_row][wanted_col] == "C":
#         santas_position = [wanted_row, wanted_col]
#         for x, y in directions.values():
#             current_row = santas_position[0] + x
#             current_col = santas_position[1] + y
#             current_home = neighborhood[current_row][current_col]
#             if current_home.isalpha():
#                 if current_home == "V":
#                     number_of_presents -= 1
#                     nice_kids_visited += 1
#                     neighborhood[current_row][current_col] = "-"
#                 elif current_home == "X":
#                     number_of_presents -= 1
#                     neighborhood[current_row][current_col] = "-"
# 
#     elif neighborhood[wanted_row][wanted_col] == "-":
#         santas_position = [wanted_row, wanted_col]
# 
#     if not number_of_presents or total_nice_kids == nice_kids_visited:
#         break
# 
#     command = input()
# 
# neighborhood[santas_position[0]][santas_position[1]] = "S"
# 
# 
# if not number_of_presents and total_nice_kids > nice_kids_visited:
#     print(f"Santa ran out of presents!")
# 
# [print(*row) for row in neighborhood]
# 
# if nice_kids_visited == total_nice_kids:
#     print(f"Good job, Santa! {total_nice_kids} happy nice kid/s.")
# else:
#     print(f"No presents for {total_nice_kids - nice_kids_visited} nice kid/s.")
