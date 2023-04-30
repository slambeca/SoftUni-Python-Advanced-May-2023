data = input()

indexes = []

for i in range(len(data)):
    char = data[i]

    if char == "(":
        indexes.append(i)
    elif char == ")":
        l = indexes.pop()
        print(data[l:i + 1])

# Variant 2
# data = input()
#
# indexes = []
#
# for index in range(len(data)):
#     if data[index] == "(":
#         indexes.append(index)
#     elif data[index] == ")":
#         starting_index = indexes.pop()
#         print(data[starting_index:index + 1])