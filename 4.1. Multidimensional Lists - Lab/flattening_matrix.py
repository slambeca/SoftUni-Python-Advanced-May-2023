rows = int(input())

matrix = []

for number in range(rows):
    numbers = [int(x) for x in input().split(", ")]

    matrix.extend(numbers)

print(matrix)

# # Variant 2
# matrix = []    # [[1, 2, 3], [4, 5, 6]]
#
# for _ in range(int(input())):
#     numbers = [int(x) for x in input().split(", ")]
#
#     matrix.append(numbers)
#
# flattened_matrix = [element for row in matrix for element in row]
#
# print(flattened_matrix)    # [1, 2, 3, 4, 5, 6]
#
# # Variant 3
# matrix = []
#
# for _ in range(int(input())):
#     numbers = list(map(int, input().split(", ")))
#     matrix.append(numbers)
#
# new_matrix = []
#
# for row in matrix:
#     for num in row:
#         new_matrix.append(num)
#
# print(new_matrix)