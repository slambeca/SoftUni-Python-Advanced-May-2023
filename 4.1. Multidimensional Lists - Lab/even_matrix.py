matrix = []

for _ in range(int(input())):
    current_row = [int(x) for x in input().split(", ") if x % 2 == 0]

    matrix.append(current_row)

print(matrix)

# # Variant 2
# matrix = []
#
# for i in range(int(input())):
#     row = input().split(", ")
#     matrix.append(list(map(int, row)))
#
# evens = [[x for x in row if x % 2 == 0] for row in matrix]
#
# print(evens)