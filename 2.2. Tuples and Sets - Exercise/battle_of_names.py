current_row = 1

odd_set = set()
even_set = set()

for _ in range(int(input())):    # 4
    name = input()    # Pesho

    total_ascii_score = 0    # 511

    for letter in name:
        total_ascii_score += ord(letter)

    divided_sum = int(total_ascii_score / current_row)    # 511

    if divided_sum % 2 == 0:
        even_set.add(divided_sum)
    else:
        odd_set.add(divided_sum)

    current_row += 1

if sum(odd_set) == sum(even_set):
    print(*odd_set.union(even_set), sep=", ")
elif sum(odd_set) > sum(even_set):
    print(*odd_set.difference(even_set), sep=", ")
elif sum(odd_set) < sum(even_set):
    print(*odd_set.symmetric_difference(even_set), sep=", ")

# Variant 2
# odd_set = set()
# even_set = set()
#
# for row in range(1, int(input()) + 1):
#     ascii_sum_of_name = sum(ord(l) for l in input()) // row  # or math floor
#
#     if ascii_sum_of_name % 2 == 0:
#         even_set.add(ascii_sum_of_name)
#     else:
#         odd_set.add(ascii_sum_of_name)
#
# if sum(odd_set) == sum(even_set):
#     print(*odd_set.union(even_set), sep=", ")
# elif sum(odd_set) > sum(even_set):
#     print(*odd_set.difference(even_set), sep=", ")
# else:
#     print(*odd_set.symmetric_difference(even_set), sep=", ")