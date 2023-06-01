def check_indices(r, c, n):
    if 0 <= r < n and 0 <= c < n:
        return True

    return False


SIZE = 7

matrix = []
# 12 21 18 4 20 7 11
# 9 D D D D D 10
# 15 D T T T D 3
# 2 D T B T D 19
# 17 D T T T D 6
# 22 D D D D D 14
# 5 8 23 13 16 1 24

players = input().split(", ")

player_one, player_two = players[0], players[1]    # Ivan Peter

player_one_throws, player_two_throws = 0, 0
player_one_score, player_two_score = 501, 501

for row in range(SIZE):
    matrix.append(input().split())

index = 1

while True:
    coordinates = input().split(", ")
    wanted_row = int(coordinates[0].strip("("))
    wanted_col = int(coordinates[1].strip(")"))

    if index % 2 != 0:
        player_one_throws += 1
        if check_indices(wanted_row, wanted_col, SIZE):
            if matrix[wanted_row][wanted_col].isdigit():
                player_one_score -= int(matrix[wanted_row][wanted_col])
            elif matrix[wanted_row][wanted_col] == "D":
                total_sum = 2 * (int(matrix[0][wanted_col]) + int(matrix[SIZE - 1][wanted_col]) +
                                 int(matrix[wanted_row][0]) + int(matrix[wanted_row][SIZE - 1]))
                player_one_score -= total_sum
            elif matrix[wanted_row][wanted_col] == "T":
                total_sum = 3 * (int(matrix[0][wanted_col]) + int(matrix[SIZE - 1][wanted_col]) +
                                 int(matrix[wanted_row][0]) + int(matrix[wanted_row][SIZE - 1]))
                player_one_score -= total_sum

            if matrix[wanted_row][wanted_col] == "B" or player_one_score <= 0:
                print(f"{player_one} won the game with {player_one_throws} throws!")
                break

    elif index % 2 == 0:
        player_two_throws += 1
        if check_indices(wanted_row, wanted_col, SIZE):
            if matrix[wanted_row][wanted_col].isdigit():
                player_two_score -= int(matrix[wanted_row][wanted_col])
            elif matrix[wanted_row][wanted_col] == "D":
                total_sum = 2 * (int(matrix[0][wanted_col]) + int(matrix[SIZE - 1][wanted_col]) +
                                 int(matrix[wanted_row][0]) + int(matrix[wanted_row][SIZE - 1]))
                player_two_score -= total_sum
            elif matrix[wanted_row][wanted_col] == "T":
                total_sum = 3 * (int(matrix[0][wanted_col]) + int(matrix[SIZE - 1][wanted_col]) +
                                 int(matrix[wanted_row][0]) + int(matrix[wanted_row][SIZE - 1]))
                player_two_score -= total_sum

            if matrix[wanted_row][wanted_col] == "B" or player_two_score <= 0:
                print(f"{player_two} won the game with {player_two_throws} throws!")
                break

    index += 1