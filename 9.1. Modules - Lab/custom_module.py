# This custom module is for exercise 3.triangle


def draw_triangle(n):
    for i in range(1, n + 1):
        row = ""
        for j in range(1, i + 1):
            row += str(j)
        print(' '.join(row))

    for x in range(n, 1, -1):
        new_row = ""
        for y in range(1, x):
            new_row += str(y)
        print(' '.join(new_row))