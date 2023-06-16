def get_magic_triangle(number):
    magic_triangle = [[1], [1, 1]]

    if number == 2:
        return magic_triangle

    for i in range(2, number):
        current_row = [1]
        previous_row = magic_triangle[i - 1]

        for j in range(1, i):
            current_row.append(previous_row[j - 1] + previous_row[j])

        current_row.append(1)
        magic_triangle.append(current_row)

    return magic_triangle


print(get_magic_triangle(5))