def check_valid_index(indexes):
    if {indexes[0], indexes[2]}.issubset(valid_rows) and {indexes[1], indexes[3]}.issubset(valid_columns):
        return True

    return False


def swap_coordinates(command, indexes):
    if check_valid_index(indexes) and command == "swap" and len(indexes) == 4:
        row1, col1, row2, col2 = indexes

        matrix[row1][col1], matrix[row2][col2] = matrix[row2][col2], matrix[row1][col1]

        print(*[' '.join(matrix[r]) for r in range(rows)], sep="\n")
    else:
        print("Invalid input!")


rows, columns = [int(x) for x in input().split()]
matrix = [input().split() for _ in range(rows)]    # [['1', '2', '3'], ['4', '5', '6']]

valid_rows = range(rows)
valid_columns = range(columns)

while True:
    command_type, *info = [int(x) if x.isdigit() else x for x in input().split()]

    if command_type == "END":
        break

    swap_coordinates(command_type, info)

# Variant 2
# rows, cols = [int(x) for x in input().split()]
# 
# matrix = [input().split() for _ in range(rows)]
# 
# COMMAND_END = "END"
# 
# valid_rows = list(range(rows))
# valid_cols = list(range(cols))
# 
# while True:
#     command, *info = [int(x) if x.isdigit() else x for x in input().split()]
# 
#     if len(info) == 4 and command == "swap":
#         row_one, col_one, row_two, col_two = info
#         if {row_one, row_two}.issubset(valid_rows) and {col_one, col_two}.issubset(valid_cols):
#             matrix[row_one][col_one], matrix[row_two][col_two] = matrix[row_two][col_two], matrix[row_one][col_one]
#             [print(*row) for row in matrix]
#         else:
#             print("Invalid input!")
#             continue
#     elif command == COMMAND_END:
#         break
#     else:
#         print("Invalid input!")
#         continue
