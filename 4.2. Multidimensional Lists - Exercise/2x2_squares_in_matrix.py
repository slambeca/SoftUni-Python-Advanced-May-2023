rows, columns = [int(x) for x in input().split()]

matrix = []

for i in range(rows):
    elements = [x for x in input().split()]
    matrix.append(elements)

equal_squares = 0

for row in range(rows - 1):
    for column in range(columns - 1):
        first = matrix[row][column]
        second = matrix[row][column + 1]
        third = matrix[row + 1][column]
        fourth = matrix[row + 1][column + 1]
        if first == second == third == fourth:
            equal_squares += 1

print(equal_squares)

# Variant 2
# rows, columns = [int(x) for x in input().split()]
# matrix = [input().split() for _ in range(rows)]
#
# equal_block = 0
#
# for row in range(rows - 1):
#     for column in range(columns - 1):
#         symbol = matrix[row][column]
#
#         if matrix[row][column + 1] == symbol and matrix[row + 1][column] == symbol \
#                 and matrix[row + 1][column + 1] == symbol:
#             equal_block += 1
#
# print(equal_block)

# Variant 3
# rows, cols = [int(x) for x in input().split()]
#
# matrix = [[x for x in input().split()] for _ in range(rows)]
#
# counter = 0
#
# for i in range(rows - 1):
#     for j in range(cols - 1):
#         if matrix[i][j] == matrix[i][j + 1] == matrix[i + 1][j] == matrix[i + 1][j + 1]:
#             counter += 1
#
# print(counter)
