def fill_the_box(*args):
    height, length, width, *data = args
    size_of_the_box = height * length * width
    left_boxes = 0
    for symbol in data:
        if symbol == "Finish":
            break
        if size_of_the_box - symbol <= 0:
            symbol -= size_of_the_box
            size_of_the_box = 0
        if size_of_the_box > 0:
            size_of_the_box -= symbol
        else:
            left_boxes += symbol

    if size_of_the_box > 0:
        return f"There is free space in the box. You could put {size_of_the_box} more cubes."

    return f"No more free space! You have {left_boxes} more cubes."


print(fill_the_box(2, 8, 2, 2, 1, 7, 3, 1, 5, "Finish"))
print(fill_the_box(5, 5, 2, 40, 11, 7, 3, 1, 5, "Finish"))
print(fill_the_box(10, 10, 10, 40, "Finish", 2, 15, 30))

# Variant 2
# def fill_the_box(height, length, width, *data):
#     space = height * length * width
#     cubes_left = 0

#     for item in data:
#         if item == "Finish":
#             break
#         left_from_cube = item - space
#         space -= item

#         if space < 0:
#             cubes_left += left_from_cube
#             space = 0

#     if space:
#         return f"There is free space in the box. You could put {space} more cubes."

#     return f"No more free space! You have {cubes_left} more cubes."


# print(fill_the_box(2, 8, 2, 2, 1, 7, 3, 1, 5, "Finish"))
# print(fill_the_box(5, 5, 2, 40, 11, 7, 3, 1, 5, "Finish"))
# print(fill_the_box(10, 10, 10, 40, "Finish", 2, 15, 30,))
