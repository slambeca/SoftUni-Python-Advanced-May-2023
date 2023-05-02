from collections import deque

collected_honey = 0

functions = {
    "+": lambda a, b: a + b,
    "-": lambda a, b: a - b,
    "*": lambda a, b: a * b,
    "/": lambda a, b: a / b
}

workings_bees = deque([int(x) for x in input().split()])    # deque([20, 62, 99, 35, 0, 150])
nectar = deque([int(x) for x in input().split()])    # deque([120, 60, 10, 1, 70, 10])
waiting_bees = deque(input().split())    # deque(['+', '-', '+', '+', '/', '*', '-', '-', '/'])

while workings_bees and nectar:
    bee = workings_bees.popleft()    # 20
    current_nectar = nectar.pop()    # 10

    if current_nectar >= bee:    # It is considered collected, the bee can return to the hive
        if current_nectar != 0:    # We can not divide by zero!
            collected_honey += abs(functions[waiting_bees.popleft()](bee, current_nectar))    # We take the first symbol

    elif current_nectar < bee:
        workings_bees.appendleft(bee)

print(f"Total honey made: {collected_honey}")
if workings_bees:
    print(f"Bees left: {', '.join(str(x) for x in workings_bees)}")
if nectar:
    print(f"Nectar left: {', '.join(str(x) for x in nectar)}")

# Variant 2
# from collections import deque
#
# bees = deque(int(x) for x in input().split())
# nectar = deque(int(x) for x in input().split())
#
# symbols = deque(input().split())
#
# total_honey = 0
#
# operations = {
#     "*": lambda x, y: x * y,
#     "/": lambda x, y: x / y,
#     "-": lambda x, y: x - y,
#     "+": lambda x, y: x + y,
# }
#
# while bees and nectar:
#     current_bee = bees.popleft()
#     current_nectar = nectar.pop()
#
#     if current_nectar < current_bee:
#         bees.appendleft(current_bee)
#     elif current_nectar > current_bee:
#         total_honey += abs(operations[symbols.popleft()](current_bee, current_nectar))
#
# print(f"Total honey made: {total_honey}")
# if bees:
#     print(f"Bees left: {', '.join(str(x) for x in bees)}")
# if nectar:
#     print(f"Nectar left: {', '.join(str(x) for x in nectar)}")
#
# # Variant 3
# from collections import deque
#
# collected_honey = 0
#
# functions = {
#     "+": lambda a, b: a + b,
#     "-": lambda a, b: a - b,
#     "*": lambda a, b: a * b,
#     "/": lambda a, b: a / b
# }
#
# workings_bees = deque([int(x) for x in input().split()])    # deque([20, 62, 99, 35, 0, 150])
# nectar = deque([int(x) for x in input().split()])    # deque([120, 60, 10, 1, 70, 10])
# waiting_bees = deque(input().split())    # deque(['+', '-', '+', '+', '/', '*', '-', '-', '/'])
#
# while workings_bees and nectar:
#     bee = workings_bees.popleft()    # 20
#     current_nectar = nectar.pop()    # 10
#
#     if current_nectar > bee:    # It is considered collected, the bee can return to the hive
#         collected_honey += abs(functions[waiting_bees.popleft()](bee, current_nectar))    # We take the first symbol
#
#     elif current_nectar < bee:
#         workings_bees.appendleft(bee)
#
# print(f"Total honey made: {collected_honey}")
# if workings_bees:
#     print(f"Bees left: {', '.join(str(x) for x in workings_bees)}")
# if nectar:
#     print(f"Nectar left: {', '.join(str(x) for x in nectar)}")