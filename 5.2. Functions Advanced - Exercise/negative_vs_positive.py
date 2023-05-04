numbers = [int(x) for x in input().split()]


def positive_sum(some_array):
    global total_positive_sum
    for num in some_array:
        if num > 0:
            total_positive_sum += num

    return total_positive_sum


def negative_sum(some_array):
    global total_negative_sum
    for num in some_array:
        if num < 0:
            total_negative_sum += num

    return total_negative_sum


def compare_sums(some_negative_sum, some_positive_sum):
    if abs(some_negative_sum) > some_positive_sum:
        return "The negatives are stronger than the positives"

    return "The positives are stronger than the negatives"


total_positive_sum = 0
total_negative_sum = 0

print(negative_sum(numbers))
print(positive_sum(numbers))
# negative_sum = sum(n for n in numbers if n < 0)
# positive_sum = sum(n for n in numbers if n > 0)
print(compare_sums(total_negative_sum, total_positive_sum))

# Variant 2
#
#
# def sum_negative():
#     sum_of_numbers = 0
#
#     for num in numbers:
#         if num < 0:
#             sum_of_numbers += num
#
#     return sum_of_numbers
#
#
# def sum_positive():
#     sum_of_numbers = 0
#
#     for num in numbers:
#         if num > 0:
#             sum_of_numbers += num
#
#     return sum_of_numbers
#
#
# def print_result(positive, negative):
#     print(negative)
#     print(positive)
#
#     if positive > abs(negative):
#         print("The positives are stronger than the negatives")
#     else:
#         print("The negatives are stronger than the positives")
#
#
# numbers = [int(x) for x in input().split()]
#
# negative_numbers = sum_negative()
# positive_numbers = sum_positive()
#
# print_result(positive_numbers, negative_numbers)