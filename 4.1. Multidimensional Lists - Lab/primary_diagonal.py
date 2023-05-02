def read_matrix():
    rows = int(input())
    current_matrix = []

    for row in range(rows):
        current_matrix.append(list(map(int, input().split())))

    return current_matrix


def get_sum_primary_diagonal():
    matrix = read_matrix()
    rows = len(matrix)
    columns = len(matrix[0])
    sum_columns = []

    for i in range(columns):    # 0 1 2
        current_sum = 0
        index = 0
        for j in range(rows):    # 0 1 2
            current_sum += matrix[index][index]
            index += 1

        sum_columns.append(current_sum)

    return sum_columns


print(*set(get_sum_primary_diagonal()))

# # Variant 2
#
#
# def read_matrix():
#     rows = int(input())
#     current_matrix = []
#
#     for row in range(rows):
#         current_matrix.append(list(map(int, input().split())))
#
#     return current_matrix
#
#
# matrix = read_matrix()
#
#
# def get_sum_primary_diagonal(matrix):
#     sum_of_primary_diagonal = [matrix[i][i] for i in range(len(matrix))]
#     return sum(sum_of_primary_diagonal)
#
#
# print(get_sum_primary_diagonal(matrix))