count_input_lines = int(input())

my_set = set()

for _ in range(count_input_lines):
    elements = input().split()
    for element in elements:
        my_set.add(element)

print(*my_set, sep="\n")

# # Variant 2
# elements = set()
#
# for _ in range(int(input())):
#     for el in input().split():
#         elements.add(el)
#
# print(*elements, sep="\n")
#
# # Variant 3
# elements = []
#
# for _ in range(int(input())):
#     elements.extend(input().split())
#
# print(*set(elements), sep="\n")