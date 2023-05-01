result = set(input() for username in range(int(input())))

print("\n".join(result))

# Variant 2
# print("\n".join(set(input() for username in range(int(input())))))
#
# # Variant 3
# names_count = int(input())
# names = set()
#
# for _ in range(names_count):
#     names.add(input())
#
# print(*names, sep="\n")
#
# # Variant 4
# print(*{input() for _ in range(int(input()))}, sep="\n")