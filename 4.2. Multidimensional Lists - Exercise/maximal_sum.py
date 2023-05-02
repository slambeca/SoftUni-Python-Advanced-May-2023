rows, columns = [int(x) for x in input().split()]
matrix = [[int(x) for x in input().split()] for _ in range(rows)]
# [[1, 5, 5, 2, 4], [2, 1, 4, 14, 3], [3, 7, 11, 2, 8], [4, 8, 12, 16, 4]]

maximum_sum = 0
maximum_first = 0
maximum_second = 0
maximum_third = 0
maximum_fourth = 0
maximum_fifth = 0
maximum_sixth = 0
maximum_seventh = 0
maximum_eighth = 0
maximum_ninth = 0

for row in range(rows - 2):
    for column in range(columns - 2):
        first = matrix[row][column]
        second = matrix[row][column + 1]
        third = matrix[row][column + 2]
        fourth = matrix[row + 1][column]
        fifth = matrix[row + 1][column + 1]
        sixth = matrix[row + 1][column + 2]
        seventh = matrix[row + 2][column]
        eighth = matrix[row + 2][column + 1]
        ninth = matrix[row + 2][column + 2]
        total_sum = first + second + third + fourth + fifth + sixth + seventh + eighth + ninth
        if total_sum > maximum_sum:
            maximum_sum = total_sum
            maximum_first = first
            maximum_second = second
            maximum_third = third
            maximum_fourth = fourth
            maximum_fifth = fifth
            maximum_sixth = sixth
            maximum_seventh = seventh
            maximum_eighth = eighth
            maximum_ninth = ninth

print(f"Sum = {maximum_sum}")
print(f"{maximum_first} {maximum_second} {maximum_third}\n{maximum_fourth} {maximum_fifth} {maximum_sixth}\n"
      f"{maximum_seventh} {maximum_eighth} {maximum_ninth}")

# # Variant 2
# rows, columns = [int(x) for x in input().split()]
# matrix = [[int(x) for x in input().split()] for _ in range(rows)]
#
# max_sum = float("-inf")
# biggest_matrix = []
#
# for row in range(rows - 2):
#     for column in range(columns - 2):
#         first_row = matrix[row][column:column + 3]
#         second_row = matrix[row + 1][column:column + 3]
#         third_row = matrix[row + 2][column:column + 3]
#
#         current_sum = sum(first_row) + sum(second_row) + sum(third_row)
#
#         if current_sum > max_sum:
#             max_sum = current_sum
#             biggest_matrix = [first_row, second_row, third_row]
#
# print(f"Sum = {max_sum}")
# [print(*biggest_matrix[row]) for row in range(3)]