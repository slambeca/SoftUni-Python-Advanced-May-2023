def operate(operator, *args):
    result = args[0]
    if operator == "+":
        result = sum(args)
    elif operator == "-":
        for num in args[1:]:
            result -= num
    elif operator == "*":
        for num in args[1:]:
            result *= num
    elif operator == "/":
        for num in args[1:]:
            result /= num

    return result

# Variant 2
# from functools import reduce
#
#
# def operate(operator, *args):
#     if operator == "+":
#         return reduce(lambda x, y: x + y, args)
#     elif operator == "-":
#         return reduce(lambda x, y: x - y, args)
#     elif operator == "*":
#         return reduce(lambda x, y: x * y, args)
#     elif operator == "/":
#         return reduce(lambda x, y: x / y, args)
#
#
# print(operate("+", 1, 2, 3))
# print(operate("*", 3, 4))

# Variant 3
# from functools import reduce
# 
# 
# def operate(operator, *args):
#     return reduce(lambda a, b: eval(f"{a}{operator}{b}"), args)
