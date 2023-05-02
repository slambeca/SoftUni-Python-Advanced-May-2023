first_set = {int(x) for x in input().split()}    # {1, 2, 3, 4, 5}
second_set = {int(x) for x in input().split()}    # {1, 2, 3}

for _ in range(int(input())):    # 3
    command = input()

    first, second, *numbers = command.split()

    if "Add First" in command:
        [first_set.add(int(number)) for number in numbers]
    elif "Add Second" in command:
        [second_set.add(int(number)) for number in numbers]
    if "Remove First" in command:
        [first_set.discard(int(number)) for number in numbers]
    elif "Remove Second" in command:
        [second_set.discard(int(number)) for number in numbers]
    else:
        if first_set.issubset(second_set) or second_set.issubset(first_set):
            print("True")
        else:
            print("False")

print(*sorted(first_set), sep=", ")
print(*sorted(second_set), sep=", ")

# Variant 2
# first = set(int(x) for x in input().split())
# second = set(int(x) for x in input().split())
#
# for _ in range(int(input())):
#     first_command, *data = input().split()
#
#     command = first_command + " " + data.pop(0)    # Add First, Add Second, etc.
#
#     if command == "Add First":
#         [first.add(int(element)) for element in data]
#     elif command == "Add Second":
#         [second.add(int(element)) for element in data]
#     elif command == "Remove First":
#         [first.discard(int(element)) for element in data]
#     elif command == "Remove Second":
#         [second.discard(int(element)) for element in data]
#     else:
#         if first.issubset(second) or second.issubset(first_command):
#             print("True")
#         else:
#             print("False")
#
# print(*sorted(first), sep=", ")
# print(*sorted(second), sep=", ")
#
# # Variant 3
# first = set(int(x) for x in input().split())
# second = set(int(x) for x in input().split())
#
# functions = {
#     "Add First": lambda x: [first.add(el) for el in x],
#     "Add Second": lambda x: [second.add(el) for el in x],
#     "Remove First": lambda x: [first.discard(el) for el in x],
#     "Remove Second": lambda x: [second.discard(el) for el in x],
#     "Check Subset": lambda: print("True") if first.issubset(second) or second.issubset(first) else print("False")
# }
#
# for _ in range(int(input())):
#     first_command, *data = input().split()
#
#     command = first_command + " " + data.pop(0)    # Add First, Add Second, etc.
#
#     if data:
#         functions[command]([int(x) for x in data])
#     else:
#         functions[command]()
#
# print(*sorted(first), sep=", ")
# print(*sorted(second), sep=", ")