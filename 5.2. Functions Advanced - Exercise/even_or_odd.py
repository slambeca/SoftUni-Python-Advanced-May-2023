def even_odd(*args):
    command = args[-1]
    result = []
    for n in args[:-1]:
        if n % 2 == 0 and command == "even":
            result.append(n)
        elif n % 2 != 0 and command == "odd":
            result.append(n)

    return result


print(even_odd(1, 2, 3, 4, 5, 6, "even"))
print(even_odd(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "odd"))


# Variant 2
#
#
# def even_odd(*args):
#     command = args[-1]
#
#     if command == "even":
#         return [x for x in args[:-1] if x % 2 == 0]
#     else:
#         return [x for x in args[:-1] if x % 2 != 0]
#
#
# print(even_odd(1, 2, 3, 4, 5, 6, "even"))
# print(even_odd(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "odd"))