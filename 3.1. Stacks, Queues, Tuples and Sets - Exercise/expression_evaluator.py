from functools import reduce
from math import floor

expression = input().split()    # ['6', '3', '-', '2', '1', '*', '5', '/']

idx = 0

functions = {
    "*": lambda i: reduce(lambda a, b: int(a) * int(b), expression[:i]),
    "/": lambda i: reduce(lambda a, b: int(a) / int(b), expression[:i]),
    "+": lambda i: reduce(lambda a, b: int(a) + int(b), expression[:i]),
    "-": lambda i: reduce(lambda a, b: int(a) - int(b), expression[:i]),
}

while idx < len(expression):
    element = expression[idx]

    if element in "*/+-":
        result = functions[element](idx)
        [expression.pop(1) for i in range(idx)]
        expression[0] = result
        idx = 0

    idx += 1

print(floor(int(expression[0])))

# Variant 2
# from collections import deque
#
# numbers = deque()
#
# expression = input().split()    # ['6', '3', '-', '2', '1', '*', '5', '/']
#
# functions = {
#     "*": lambda f, s: f * s,
#     "/": lambda f, s: f // s,
#     "+": lambda f, s: f + s,
#     "-": lambda f, s: f - s,
# }
#
# for element in expression:
#     if element in "-+*/":
#         while len(numbers) > 1:
#             numbers.appendleft(functions[element](numbers.popleft(), numbers.popleft()))
#     else:
#         numbers.append(int(element))
#
# print(numbers.popleft())

# Variant 3
# from collections import deque
# from math import floor
# 
# expression = deque(input().split())
# 
# idx = 0
# 
# while idx < len(expression):
#     element = expression[idx]
# 
#     if element == "*":
#         for _ in range(idx - 1):
#             expression.appendleft(int(expression.popleft()) * int(expression.popleft()))
#     elif element == "/":
#         for _ in range(idx - 1):
#             expression.appendleft(int(expression.popleft()) / int(expression.popleft()))
#     elif element == "+":
#         for _ in range(idx - 1):
#             expression.appendleft(int(expression.popleft()) + int(expression.popleft()))
#     elif element == "-":
#         for _ in range(idx - 1):
#             expression.appendleft(int(expression.popleft()) - int(expression.popleft()))
# 
#     if element in "*/+-":
#         del expression[1]
#         idx = 1
# 
#     idx += 1
# 
# print(floor(int(expression[0])))
