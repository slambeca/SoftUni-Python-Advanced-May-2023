def read_matrix():
    """
    This functions returns a matrix
    :return: Matrix
    """
    current_matrix = [[int(x) for x in input().split()] for _ in range(int(input()))]

    return current_matrix


def get_sum_primary_diagonal(some_matrix):    # [0][0] [1][1] [2][2]
    """
    This functions finds the sum of the numbers in the primary diagonal of the matrix
    :param some_matrix:
    :return: Returns the sum of those numbers
    """
    sum_of_primary_diagonal = [some_matrix[i][i] for i in range(len(some_matrix))]

    return sum(sum_of_primary_diagonal)


def get_sum_secondary_diagonal(some_matrix):    # [0][2] [1][1] [2][0]
    """
    This functions finds the sum of the numbers in the secondary diagonal of the matrix
    :param some_matrix:
    :return: Returns the sum of those numbers
    """
    index = 0
    numbers = []
    for i in range(len(some_matrix) - 1, -1, -1):
        numbers.append(some_matrix[index][i])
        index += 1

    return sum(numbers)


matrix = read_matrix()    # [[11, 2, 4], [4, 5, 6], [10, 8, -12]]

primary_diagonal_numbers = get_sum_primary_diagonal(matrix)
sum_primary_diagonal = get_sum_primary_diagonal(matrix)
secondary_diagonal_numbers = get_sum_secondary_diagonal(matrix)
sum_secondary_diagonal = get_sum_secondary_diagonal(matrix)
difference = abs(sum_primary_diagonal - sum_secondary_diagonal)

print(difference)

# # Variant 2
# n = int(input())
#
# matrix = [[int(x) for x in input().split()] for _ in range(n)]
#
# sum_primary_diagonal = sum([matrix[r][r] for r in range(n)])
# sum_secondary_diagonal = sum([matrix[r][n - r - 1] for r in range(n - 1, -1, -1)])
#
# print(abs(sum_primary_diagonal - sum_secondary_diagonal))
#
# # Variant 3
# n = int(input())
#
# matrix = [[int(x) for x in input().split()] for _ in range(n)]
#
# primary, secondary = 0, 0
#
# for i in range(n):
#     primary += matrix[i][i]
#     secondary += matrix[n - i - 1][i]
#
# print(abs(primary - secondary))