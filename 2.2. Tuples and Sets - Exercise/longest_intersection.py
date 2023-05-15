count_lines = int(input())

longest_intersection = []

for _ in range(count_lines):
    ranges = input().split("-")    # ['0,3', '1,2']

    first_data = ranges[0]    # 0,3
    second_data = ranges[1]    # 1,2

    start_index_set_one, end_index_set_one = first_data.split(",")
    start_index_set_two, end_index_set_two = second_data.split(",")

    first_set = set(range(int(start_index_set_one), int(end_index_set_one) + 1))
    second_set = set(range(int(start_index_set_two), int(end_index_set_two) + 1))

    intersection = first_set.intersection(second_set)

    if len(intersection) > len(longest_intersection):
        longest_intersection = list(intersection)

print(f"Longest intersection is {longest_intersection} with length {len(longest_intersection)}")

# Variant 2
# longest_intersection = set()
#
# for _ in range(int(input())):
#     first_data, second_data = [el.split(",") for el in input().split("-")]
#
#     first_range = set(range(int(first_data[0]), int(first_data[1]) + 1))
#     second_range = set(range(int(second_data[0]), int(second_data[1]) + 1))
#
#     intersection = first_range.intersection(second_range)
#
#     if len(intersection) > len(longest_intersection):
#         longest_intersection = intersection
#
# print(f"Longest intersection is "
#       f"[{', '.join([str(x) for x in longest_intersection])}] "
#       f"with length {len(longest_intersection)}")

# Variant 3, similar to Variant 2
# longest_intersection = set()
#
# for _ in range(int(input())):
#     first_data, second_data = [element.split(",") for element in input().split("-")]
#
#     first_range = set(range(int(first_data[0]), int(first_data[1]) + 1))
#     second_range = set(range(int(second_data[0]), int(second_data[1]) + 1))
#
#     intersection = first_range.intersection(second_range)
#
#     if len(intersection) > len(longest_intersection):
#         longest_intersection = intersection
#
# print(f"Longest intersection is {list(longest_intersection)} with length {len(longest_intersection)}")
