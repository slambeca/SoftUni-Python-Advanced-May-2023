def check_indexes(r, c, some_matrix):
    if 0 <= r < len(some_matrix) and 0 <= c < len(some_matrix):
        return True
    return False


def check_value(value):
    if value > 0:
        return True
    return False


matrix = [[int(x) for x in input().split()] for _ in range(int(input()))]
# [[8, 3, 2, 5], [6, 4, 7, 9], [9, 9, 3, 6], [6, 8, 1, 2]]

coordinates = input().split()    # ['1,2', '2,1', '2,0']

for coordinate in range(len(coordinates)):    # 3
    row = int(coordinates[coordinate][0])    # 1
    column = int(coordinates[coordinate][2])    # 2
    current_coordinate = matrix[row][column]    # 7
    if not check_value(current_coordinate):    # Very important check!
        continue
    matrix[row][column] = 0    # The bomb explodes
    if check_indexes((row - 1), (column - 1), matrix):
        if check_value(matrix[row - 1][column - 1]):
            matrix[row - 1][column - 1] -= current_coordinate
    if check_indexes((row - 1), column, matrix):
        if check_value(matrix[row - 1][column]):
            matrix[row - 1][column] -= current_coordinate
    if check_indexes((row - 1), (column + 1), matrix):
        if check_value(matrix[row - 1][column + 1]):
            matrix[row - 1][column + 1] -= current_coordinate
    if check_indexes(row, (column - 1), matrix):
        if check_value(matrix[row][column - 1]):
            matrix[row][column - 1] -= current_coordinate
    if check_indexes((row + 1), (column - 1), matrix):
        if check_value(matrix[row + 1][column - 1]):
            matrix[row + 1][column - 1] -= current_coordinate
    if check_indexes((row + 1), column, matrix):
        if check_value(matrix[row + 1][column]):
            matrix[row + 1][column] -= current_coordinate
    if check_indexes((row + 1), (column + 1), matrix):
        if check_value(matrix[row + 1][column + 1]):
            matrix[row + 1][column + 1] -= current_coordinate
    if check_indexes(row, (column + 1), matrix):
        if check_value(matrix[row][column + 1]):
            matrix[row][column + 1] -= current_coordinate

alive_cells, total_sum = 0, 0

for i in range(len(matrix)):
    for j in range(len(matrix)):
        current_cell = matrix[i][j]
        if current_cell > 0:
            alive_cells += 1
            total_sum += matrix[i][j]

print(f"Alive cells: {alive_cells}")
print(f"Sum: {total_sum}")

for element in matrix:
    print(*element)

# Variant 2
# n = int(input())
#
# matrix = [[int(x) for x in input().split()] for _ in range(int(n))]
# coordinates = ((int(x) for x in coordinate.split(",")) for coordinate in input().split())    # Tuple comprehension
#
# directions = (
#     (-1, 0),    # Up
#     (1, 0),     # Down
#     (0, 1),     # Right
#     (0, -1),    # Left
#     (-1, 1),    # Top right
#     (-1, -1),   # Top left
#     (1, -1),    # Bottom left
#     (1, 1),     # Bottom right
#     (0, 0),     # Current (this should be last)
# )
#
# for row, col in coordinates:
#     if matrix[row][col] <= 0:
#         continue
#
#     for x, y in directions:
#         r, c = row + x, col + y
#
#         if 0 <= r < n and 0 <= c < n:
#             matrix[r][c] -= matrix[row][col] if matrix[r][c] > 0 else 0
#
# alive_cells = [num for row in range(n) for num in matrix[row] if num > 0]
#
# print(f"Alive cells: {len(alive_cells)}")
# print(f"Sum: {sum(alive_cells)}")
# [print(*matrix[r], sep=" ") for r in range(n)]