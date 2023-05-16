data = [int(x) for x in input().split(", ")]

matrix = []

rows = int(data[0])    # 3
columns = int(data[1])    # 6 - we don`t use it in this case

for i in range(rows):
    numbers = [int(x) for x in input().split(", ")]

    matrix.append(numbers)

total_sum = sum([sum(x) for x in matrix])

print(total_sum)
print(matrix)

# Variant 2
#
#
# def read_matrix_func():
#     number_of_rows, number_of_columns = map(int, input().split(", "))
#     current_matrix = []
#
#     for row in range(number_of_rows):
#         numbers = list(map(int, input().split(", ")))
#         current_matrix.append(numbers)
#
#     return current_matrix
#
#
# matrix = read_matrix_func()
#
# matrix_elements_sum = 0
#
# for i in range(len(matrix)):
#     current_row = matrix[i]
#     matrix_elements_sum += sum(current_row)
#
# print(matrix_elements_sum)
# print(matrix)
#
# Variant 3
# data = list(int(x) for x in input().split(", "))
#
# rows = int(data[0])
# columns = data[1]
#
# matrix = []
#
# total_sum = 0
#
# for _ in range(rows):
#     numbers = [int(x) for x in input().split(", ")]
#
#     matrix.append(numbers)
#
#     total_sum += sum(numbers)
#
# print(total_sum)
# print(matrix)

# Variant 4
# rows, cols = [int(x) for x in input().split(", ")]
# 
# matrix = []
# 
# total_sum = 0
# 
# for _ in range(rows):
#     inner_list = [int(x) for x in input().split(", ")]
#     matrix.append(inner_list)
# 
# for row_index in range(rows):
#     for col_index in range(cols):
#         total_sum += matrix[row_index][col_index]
# 
# print(total_sum)
# print(matrix)
