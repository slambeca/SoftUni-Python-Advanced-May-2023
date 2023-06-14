SIZE = 6

matrix = [[x for x in input().split()] for _ in range(SIZE)]

total_sum = 0
prize = None

for _ in range(3):
    coordinates = input().split(", ")
    row = coordinates[0]
    row = int(row[1])    # 1 -> this part here does not work correctly in all cases
    column = coordinates[1]
    column = int(column[0])    # 1 -> this part here does not work correctly in all cases
    if 0 <= row < SIZE and 0 <= column < SIZE:    # We check if the indexes are valid
        if matrix[row][column] == "B":
            matrix[row][column] = "X"
            for r in range(SIZE):
                for c in range(SIZE):
                    current_element = matrix[r][c]
                    if c == column and current_element.isdigit():
                        total_sum += int(current_element)


if 100 <= total_sum <= 199:
    prize = "Football"
elif 200 <= total_sum <= 299:
    prize = "Teddy Bear"
elif total_sum >= 300:
    prize = "Lego Construction Set"

if not prize:
    print(f"Sorry! You need {100 - total_sum} points more to win a prize.")
else:
    print(f"Good job! You scored {total_sum} points, and you've won {prize}.")

# Variant 2


# def check_indices(r, c, n):
#     if 0 <= r < n and 0 <= c < n:
#         return True
#
#     return False
#
#
# SIZE = 6
#
# NUMBER_OF_THROWS = 3
#
# points_scored = 0
#
# prize_won = None
#
# board = []
# # 10 30 B 4 20 24
# # 7 8 27 23 11 19
# # 13 3 14 B 17 В
# # 12 5 21 22 9 6
# # B 26 1 28 29 2
# # 25 B 16 15 B 18
#
# for _ in range(SIZE):
#     board.append(input().split())
#
# for _ in range(NUMBER_OF_THROWS):
#     coordinates = input().split(", ")    # ['(1', '1)']
#     wanted_row = int(coordinates[0].strip("("))
#     wanted_col = int(coordinates[1].strip(")"))
#     if check_indices(wanted_row, wanted_col, SIZE):
#         if board[wanted_row][wanted_col] == "B":
#             board[wanted_row][wanted_col] = "X"
#             for row in range(SIZE):
#                 for col in range(SIZE):
#                     current_element = board[row][col]
#                     if col == wanted_col and current_element.isdigit():
#                         points_scored += int(board[row][col])
#
# if 100 <= points_scored <= 199:
#     prize_won = "Football"
# elif 200 <= points_scored <= 299:
#     prize_won = "Teddy Bear"
# elif points_scored >= 300:
#     prize_won = "Lego Construction Set"
#
# if prize_won:
#     print(f"Good job! You scored {points_scored} points, and you've won {prize_won}.")
# else:
#     print(f"Sorry! You need {100 - points_scored} points more to win a prize.")

# Variant 3
# def check_indices(r, c, size):
#     if 0 <= r < size and 0 <= c < size:
#         return True

#     return False


# SIZE = 6
# THROWS = 3
# prize_won = ""

# matrix = []
# # 10 30 B 4 20 24
# # 7 8 27 23 11 19
# # 13 3 14 B 17 В
# # 12 5 21 22 9 6
# # B 26 1 28 29 2
# # 25 B 16 15 B 18

# total_points = 0

# for row in range(SIZE):
#     matrix.append(input().split())

# for _ in range(THROWS):
#     coordinates = input().split(", ")
#     wanted_row = int(coordinates[0].strip("("))
#     wanted_col = int(coordinates[1].strip(")"))

#     if not check_indices(wanted_row, wanted_col, SIZE) or matrix[wanted_row][wanted_col] != "B":
#         continue

#     if matrix[wanted_row][wanted_col] == "B":
#         matrix[wanted_row][wanted_col] = 0
#         for row in range(SIZE):
#             for col in range(SIZE):
#                 if col == wanted_col:
#                     total_points += int(matrix[row][col])

# if 100 <= total_points <= 199:
#     prize_won = "Football"
# elif 200 <= total_points <= 299:
#     prize_won = "Teddy Bear"
# elif total_points >= 300:
#     prize_won = "Lego Construction Set"

# if not prize_won:
#     print(f"Sorry! You need {100 - total_points} points more to win a prize.")
# else:
#     print(f"Good job! You scored {total_points} points, and you've won {prize_won}.")
