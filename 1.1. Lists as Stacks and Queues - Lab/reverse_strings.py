string = input()    # I Love Python

reversed_string = []

for char in string[::-1]:
    reversed_string.append(char)

print(*reversed_string, sep="")    # nohtyP evoL I

# Variant 2
# stack = list(input())
#
# while len(stack):
#     element = stack.pop()
#     print(element, end="")    # nohtyP evoL I