def start_spring(**kwargs):
    dictionary, result = {}, ""

    for key, value in kwargs.items():
        if value not in dictionary.keys():
            dictionary[value] = []
        dictionary[value].append(key)

    for keys, values in dictionary.items():    # We sort the values in each list
        values.sort()

    sorted_dictionary = dict(sorted(dictionary.items(), key=lambda x: (-len(x[1]), x[0])))

    for key in sorted_dictionary.items():
        current_key = key[0]
        current_items = key[1]
        result += f"\n{current_key}:"

        for item in range(len(current_items)):
            result += f"\n-{current_items[item]}"

    return result


# example_objects = {
#     "Water Lilly": "flower",
#     "Swifts": "bird",
#     "Callery Pear": "tree",
#     "Swallows": "bird",
#     "Dahlia": "flower",
#     "Tulip": "flower",
# }
# print(start_spring(**example_objects))

# example_objects = {
#     "Swallow": "bird",
#     "Thrushes": "bird",
#     "Woodpeckers": "bird",
#     "Swallows": "bird",
#     "Warblers": "bird",
#     "Shrikes": "bird",
# }
# print(start_spring(**example_objects))
#
# example_objects = {
#     "Magnolia": "tree",
#     "Swallow": "bird",
#     "Thrushes": "bird",
#     "Pear": "tree",
#     "Cherries": "tree",
#     "Shrikes": "bird",
#     "Butterfly": "insect"
# }
# print(start_spring(**example_objects))

# Variant 2
# def start_spring(**kwargs):
#     dictionary, result = {}, ""
# 
#     for key, value in kwargs.items():
#         if value not in dictionary.keys():
#             dictionary[value] = []
#         dictionary[value].append(key)
# 
#     for key, value in dictionary.items():
#         value.sort()
# 
#     sorted_dict = dict(sorted(dictionary.items(), key=lambda x: (-len(x[1]), x[0])))
# 
#     for key, values in sorted_dict.items():
#         result += f"{key}:\n"
#         for value in values:
#             result += f"-{value}\n"
# 
#     return result
