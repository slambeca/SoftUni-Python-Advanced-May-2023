with open("numbers.txt", "r") as file:
    print(sum([int(el[:-1]) for el in file.readlines()]))

# # Variant 2 without context manager
# file = open("numbers.txt", "r")
#
# total_sum = 0
#
# for num in file:
#     total_sum += int(num)
#
# print(total_sum)
#
# file.close()
#
# # Variant 3 with rstrip()
# with open("numbers.txt", "r") as file:
#     print(sum([int(el.rstrip("\n")) for el in file.readlines()]))