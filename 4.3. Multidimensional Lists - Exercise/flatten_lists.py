line = input().split("|")

matrix = []

for substring in line[::-1]:
    matrix.extend(substring.split())    # We remove all the spaces

print(*matrix)

# Variant 2
# numbers = [string.split() for string in input().split("|")]
# print(*[' '.join(sub_list) for sub_list in numbers[::-1] if sub_list])
