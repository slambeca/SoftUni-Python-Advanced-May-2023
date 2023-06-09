def read_matrix():
    rows = int(input())
    current_matrix = []

    for row in range(rows):
        row_data = list(input())
        current_matrix.append(row_data)

    return current_matrix


def check_for_special_symbol(matrix, symbol):
    for row in range(len(matrix)):
        for column in range(len(matrix[row])):    # Because we do not know how many columns we might have
            current_element = matrix[row][column]
            if current_element == symbol:
                return row, column


def print_function(data, symbol):
    if data:
        print(data)
    else:
        print(f"{symbol} does not occur in the matrix")


matrix = read_matrix()    # [['A', 'B', 'C'], ['D', 'E', 'F'], ['X', '!', '@']]

special_symbol = input()

print_function(check_for_special_symbol(matrix, special_symbol), special_symbol)

# Variant 2
# rows = int(input())
# 
# matrix = []
# 
# is_found = False
# 
# for _ in range(rows):
#     current_row = list(input())
#     matrix.append(current_row)
# 
# special_symbol = input()
# 
# for row in range(rows):
#     for col in range(rows):
#         if matrix[row][col] == special_symbol:
#             print((row, col))
#             is_found = True
#             raise SystemExit
# 
# if not is_found:
#     print(f"{special_symbol} does not occur in the matrix")
