def read_matrix():
    rows, columns = map(int, input().split(", "))
    current_matrix = []

    for row in range(rows):
        current_matrix.append(list(map(int, input().split())))

    return current_matrix


def get_sum_columns():
    matrix = read_matrix()    # [[7, 1, 3, 3, 2, 1], [1, 3, 9, 8, 5, 6], [4, 6, 7, 9, 1, 0]]
    rows = len(matrix)
    columns = len(matrix[0])
    sum_columns = []

    for i in range(columns):    # 0 1 2 3 4 5
        current_sum = 0
        for j in range(rows):    # 0 1 2
            current_sum += matrix[j][i]

        sum_columns.append(current_sum)

    return sum_columns


result = get_sum_columns()

print(*result, sep="\n")

# Variant 2
# rows, cols = [int(x) for x in input().split(", ")]
#
# matrix = []
#
# for _ in range(rows):
#     inner_list = [int(x) for x in input().split()]
#     matrix.append(inner_list)
#
# for col_index in range(cols):
#     sum_elements = 0
#     for row_index in range(rows):
#         sum_elements += matrix[row_index][col_index]
#     print(sum_elements)
