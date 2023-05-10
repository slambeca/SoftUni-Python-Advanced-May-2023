stack = []

count_queries = int(input())

COMMAND_PUSH = 1
COMMAND_DELETE = 2
COMMAND_MAXIMUM = 3
COMMAND_MINIMUM = 4

for _ in range(count_queries):
    current_query = [int(x) for x in input().split()]

    if current_query[0] == COMMAND_PUSH:
        stack.append(current_query[1])

    elif current_query[0] == COMMAND_DELETE:
        if stack:
            stack.pop()

    elif current_query[0] == COMMAND_MAXIMUM:
        if stack:
            print(max(stack))

    elif current_query[0] == COMMAND_MINIMUM:
        if stack:
            print(min(stack))

stack.reverse()

print(*stack, sep=", ")

# Variant 2 with map_functions and lambda
# from collections import deque

# numbers = deque()

# map_functions = {
#     1: lambda x: numbers.append(x[1]),
#     2: lambda x: numbers.pop() if numbers else None,
#     3: lambda x: print(max(numbers)) if numbers else None,
#     4: lambda x: print(min(numbers)) if numbers else None,
# }

# for _ in range(int(input())):
#     number_data = [int(x) for x in input().split()]

#     map_functions[number_data[0]](number_data)

# numbers.reverse()

# print(*numbers, sep=", ")

# # Variant 3
# from collections import deque

# numbers = deque()

# for _ in range(int(input())):
#     number_data = [int(x) for x in input().split()]
#     # number_data = map(int, input().split())
#     command = number_data[0]

#     if command == 1:
#         numbers.append(number_data[1])
#     elif command == 2:
#         if numbers:
#             numbers.pop()
#     elif command == 3:
#         if numbers:
#             print(max(numbers))
#     elif command == 4:
#         if numbers:
#             print(min(numbers))

# numbers.reverse()

# print(*numbers, sep=", ")

# # Variant 4, same as Variant 2
# from collections import deque

# numbers = deque()

# map_functions = {
#     1: lambda x: numbers.append(x[1]),    # x == number_data => 1, 97
#     2: lambda x: numbers.pop() if numbers else None,    # ternary operator
#     3: lambda x: print(max(numbers)) if numbers else None,
#     4: lambda x: print(min(numbers)) if numbers else None,
# }

# for _ in range(int(input())):
#     number_data = [int(x) for x in input().split()]
#     map_functions[number_data[0]](number_data)
#     # func = map_functions[number_data[0]]
#     # func(number_data)

# numbers.reverse()

# print(*numbers, sep=", ")
