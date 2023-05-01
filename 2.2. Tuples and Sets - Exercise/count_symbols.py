string = input()

dictionary = {}

for letter in string:
    if letter not in dictionary.keys():
        dictionary[letter] = 0
    dictionary[letter] += 1

for key, value in sorted(dictionary.items()):
    print(f"{key}: {value} time/s")

# Variant 2
# occurrences = {}
#
# for letter in input():
#     if letter not in occurrences.keys():
#         occurrences[letter] = 0
#     occurrences[letter] += 1
#
# for letter, times in sorted(occurrences.items()):
#     print(f"{letter}: {times} time/s")
#
# # Variant 3
# occurrences = {}
#
# for letter in input():
#     occurrences[letter] = occurrences.get(letter, 0) + 1
#
# for letter, times in sorted(occurrences.items()):
#     print(f"{letter}: {times} time/s")
#
#
# # Variant 4
# input_line = list(input())
# symbols = {symbol: input_line.count(symbol) for symbol in input_line}
#
# for key, value in sorted(symbols.items()):
#     print(f"{key}: {value} time/s")