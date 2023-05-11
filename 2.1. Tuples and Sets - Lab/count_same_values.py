numbers = [float(x) for x in input().split()]    

dictionary = {}

for number in numbers:
    if number not in dictionary.keys():
        dictionary[number] = []
    else:
        dictionary[number].append(number)

for key, values in dictionary.items():
    print(f"{key} - {len(values) + 1} times")

# Variant 2
# values = tuple(map(float, input().split())) 
#
# counter_of_values = {value: values.count(value) for value in values}
#
# for key, value in counter_of_values.items():
#     print(f"{key} - {value} times")
#
# Variant 3
# values = tuple(map(float, input().split()))  
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

# Variant 4
# numbers = tuple(input().split())
#
# occurrences = {}
#
# for el in numbers:
#     if el not in occurrences.keys():
#         occurrences[el] = 0
#     occurrences[el] += 1
#
# for key, value in occurrences.items():
#     print(f"{float(key)} - {value} times")
