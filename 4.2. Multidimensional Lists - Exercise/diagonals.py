def read_matrix():
    rows = int(input())
    current_matrix = []

    for row in range(rows):
        current_matrix.append(list(map(int, input().split(", "))))

    return current_matrix


matrix = read_matrix()    # [[1, 2, 3], [4, 5, 6], [7, 8, 9]]


def get_sum_primary_diagonal(some_matrix):    # [0][0] [1][1] [2][2]
    """
    This function finds the numbers in the primary diagonal of the matrix
    :param some_matrix:
    :return: List with numbers from the primary diagonal
    """
    sum_of_primary_diagonal = [some_matrix[i][i] for i in range(len(some_matrix))]

    return sum_of_primary_diagonal


def get_sum_secondary_diagonal(some_matrix):    # [0][2] [1][1] [2][0]
    """
    This functions finds the numbers in the secondary diagonal of the matrix
    :param some_matrix:
    :return: A list with the numbers from the secondary diagonal
    """
    index = 0
    numbers = []
    for i in range(len(some_matrix) - 1, -1, -1):
        numbers.append(some_matrix[index][i])
        index += 1

    return numbers


primary_diagonal_numbers = get_sum_primary_diagonal(matrix)
sum_primary_diagonal = sum(get_sum_primary_diagonal(matrix))
secondary_diagonal_numbers = get_sum_secondary_diagonal(matrix)
sum_secondary_diagonal = sum(get_sum_secondary_diagonal(matrix))

print(f"Primary diagonal: {', '.join(str(x) for x in primary_diagonal_numbers)}. "
      f"Sum: {sum_primary_diagonal}")
print(f"Secondary diagonal: {', '.join(str(x) for x in secondary_diagonal_numbers)}. "
      f"Sum: {sum_secondary_diagonal}")

# Variant 2
# n = int(input())
#
# matrix = [[int(x) for x in input().split(", ")] for _ in range(n)]    # [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
#
# primary_diagonal = [matrix[r][r] for r in range(n)]    # [1, 5, 9]
# secondary_diagonal = [matrix[r][n - r - 1] for r in range(n - 1, -1, -1)]   # [7, 5, 3]
#
# print(f"Primary diagonal: {', '.join(str(x) for x in primary_diagonal)}. Sum: {sum(primary_diagonal)}")
# print(f"Secondary diagonal: {', '.join([str(x) for x in secondary_diagonal][::-1])}. Sum: {sum(secondary_diagonal)}")

# Variant 3
# matrix = [[int(x) for x in input().split(", ")] for _ in range(int(input()))]
#
# primary_diagonal = [matrix[i][i] for i in range(len(matrix))]
# secondary_diagonal = [matrix[i][len(matrix) - i - 1] for i in range(len(matrix) - 1, -1, -1)]
#
# print(f"Primary diagonal: {', '.join(str(x) for x in primary_diagonal)}. Sum: {sum(primary_diagonal)}\n"
#       f"Secondary diagonal: {', '.join(str(x) for x in secondary_diagonal[::-1])}. Sum: {sum(secondary_diagonal)}")
