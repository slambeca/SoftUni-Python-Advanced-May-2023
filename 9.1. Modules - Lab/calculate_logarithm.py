from math import log

# log(n)X = y
# log(2)10^6 = 20
# log(2)1024 = 10

# n^y = X
# 2^20 = 10^6

number = int(input())
logarithm_base = input()

if logarithm_base == "natural":
    print(f"{log(number):.2f}")
else:
    print(f"{log(number, int(logarithm_base)):.2f}")

# Variant 2
# from math import log
#
#
# def calc_log(x, base):
#     if base == "natural":
#         return f"{log(x):.2f}"
#     else:
#         return f"{log(x, int(base)):.2f}"
#
#
# number = int(input())
# logarithm_base = input()
#
# print(calc_log(number, logarithm_base))