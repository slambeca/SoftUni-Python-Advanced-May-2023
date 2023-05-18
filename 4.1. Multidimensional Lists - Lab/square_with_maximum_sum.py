rows, columns = [int(x) for x in input().split(", ")]

matrix = []    # [[7, 1, 3, 3, 2, 1], [1, 3, 9, 8, 5, 6], [4, 6, 7, 9, 1, 0]]

biggest_sum = 0
biggest_first_first = 0
biggest_first_second = 0
biggest_second_first = 0
biggest_second_second = 0

for x in range(rows):
    items = [int(x) for x in input().split(", ")]
    matrix.append(items)

for i in range(rows - 1):
    for j in range(columns - 1):
        if i > (rows - 1) or j > (columns - 1):
            break
        else:
            first_first = matrix[i][j]
            first_second = matrix[i][j + 1]
            second_first = matrix[i + 1][j]
            second_second = matrix[i + 1][j + 1]

            total_sum = first_first + first_second + second_first + second_second

            if total_sum > biggest_sum:
                biggest_sum = total_sum
                biggest_first_first, biggest_first_second, biggest_second_first, biggest_second_second = \
                    first_first, first_second, second_first, second_second

print(f"{biggest_first_first} {biggest_first_second}\n{biggest_second_first} {biggest_second_second}\n{biggest_sum}")

# Variant 2
# rows, cols = [int(x) for x in input().split(", ")]

# matrix = []

# biggest_sum = 0
# biggest_first_first, biggest_first_second, biggest_second_first, biggest_second_second = [0, 0, 0, 0]

# for _ in range(rows):
#     numbers = [int(x) for x in input().split(", ")]
#     matrix.append(numbers)

# for i in range(rows - 1):
#     for j in range(cols - 1):
#         if matrix[i][j] + matrix[i][j + 1] + matrix[i + 1][j] + matrix[i + 1][j + 1] > biggest_sum:
#             biggest_sum = matrix[i][j] + matrix[i][j + 1] + matrix[i + 1][j] + matrix[i + 1][j + 1]

#             biggest_first_first, biggest_first_second, biggest_second_first, biggest_second_second = \
#                 matrix[i][j], matrix[i][j + 1], matrix[i + 1][j], matrix[i + 1][j + 1]

# print(f"{biggest_first_first} {biggest_first_second}\n{biggest_second_first} {biggest_second_second}\n{biggest_sum}")
