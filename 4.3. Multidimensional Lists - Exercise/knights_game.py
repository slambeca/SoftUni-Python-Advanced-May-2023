def check_indices(idx1, idx2, some_matrix):
    if 0 <= idx1 < len(some_matrix) and 0 <= idx2 < len(some_matrix):
        return True

    return False


n = int(input())

matrix = [list(input()) for _ in range(n)]
# [['0', 'K', '0', 'K', '0'],
# ['K', '0', '0', '0', 'K'],
# ['0', '0', 'K', '0', '0'],
# ['K', '0', '0', '0', 'K'],
# ['0', 'K', '0', 'K', '0']]

directions = (
    (-2, -1),    # Up and left
    (-2, 1),    # Up and right
    (2, -1),    # Down and left
    (2, 1),    # Down and right
    (-1, -2),    # Left and up
    (1, -2),    # Left and down
    (-1, 2),    # Right and up
    (1, 2),    # Right and down
)

removed_knights = 0

while True:
    max_attacks = 0
    knight_with_most_attacks_position = []

    for row in range(n):
        for col in range(n):
            if matrix[row][col] == "K":
                attacks = 0

                for direction in directions:
                    pos_row = row + direction[0]
                    pos_col = col + direction[1]
                    if check_indices(pos_row, pos_col, matrix):
                        if matrix[pos_row][pos_col] == "K":
                            attacks += 1

                if attacks > max_attacks:
                    max_attacks = attacks
                    knight_with_most_attacks_position = [row, col]

    if knight_with_most_attacks_position:
        r, c = knight_with_most_attacks_position
        matrix[r][c] = "0"
        removed_knights += 1
    else:
        break

print(removed_knights)