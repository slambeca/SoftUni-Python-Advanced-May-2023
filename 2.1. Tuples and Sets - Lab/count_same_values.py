numbers = [float(x) for x in input().split()]    # [-2.5, 4.0, 3.0, -2.5, -5.5, 4.0, 3.0, 3.0, -2.5, 3.0]

dictionary = {}

for number in numbers:
    if number not in dictionary.keys():
        dictionary[number] = []
    else:
        dictionary[number].append(number)

for key, values in dictionary.items():
    print(f"{key} - {len(values) + 1} times")

# # Variant 2
# values = tuple(map(float, input().split()))  # (-2.5, 4.0, 3.0, -2.5, -5.5, 4.0, 3.0, 3.0, -2.5, 3.0)
#
# counter_of_values = {value: values.count(value) for value in values}
#
# for key, value in counter_of_values.items():
#     print(f"{key} - {value} times")
#
# # Variant 3
# values = tuple(map(float, input().split()))  # (-2.5, 4.0, 3.0, -2.5, -5.5, 4.0, 3.0, 3.0, -2.5, 3.0)
#
# values_counter = {}
#
# for value in values:
#     if value not in values_counter:
#         values_counter[value] = 0
#     values_counter[value] += 1
#
# for key, value in values_counter.items():
#     print(f"{key} - {value} times")
#
# # [print(f"{key} - {value} times") for key, value in counter_of_values.items()]