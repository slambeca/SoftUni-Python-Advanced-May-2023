def multiply(*numbers):
    result = 1
    for num in numbers:
        result = result * num
    return result


print(multiply(10, 35, 60))

# # Variant 2 with reduce
# from functools import reduce
#
#
# def multiply(*args):
#     return reduce(lambda x, y: x * y, args)
#
#
# print(multiply(1, 2, 3))