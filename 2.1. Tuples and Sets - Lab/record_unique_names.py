count_names = int(input())

names = []

for _ in range(count_names):
    name = input()

    names.append(name)

print("\n".join(set(names)))

# # Variant 2
# count_names = int(input())
#
# names = set()
#
# for _ in range(count_names):
#     name = input()
#
#     names.add(name)
#
# print("\n".join(names))
#
# Variant 3
# n = int(input())
#
# names_data = {input() for _ in range(n)}
#
# for name in names_data:
#     print(name)

# Variant 4
# print(*{input() for _ in range(int(input()))}, sep="\n")
