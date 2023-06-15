def shopping_cart(*args):
    dictionary = {
        "Soup": [],
        "Pizza": [],
        "Dessert": [],
    }

    result = ""

    limits = {
        "Soup": 3,
        "Pizza": 4,
        "Dessert": 2,
    }

    for item in args:
        if item == "Stop":
            break

        type_of_meal = item[0]
        product = item[1]

        if product not in dictionary[type_of_meal] and len(dictionary[type_of_meal]) < limits[type_of_meal]:
            dictionary[type_of_meal].append(product)

    for key, value in dictionary.items():
        value.sort()

    sorted_dictionary = dict(sorted(dictionary.items(), key=lambda x: (-len(x[1]), x[0])))

    len_items = 0
    for key, values in sorted_dictionary.items():
        len_items += len(values)
        result += f"{key}:\n"
        for value in values:
            result += f" - {value}\n"

    if len_items:
        return result.strip()
    else:
        return "No products in the cart!"


# print(shopping_cart(
#     ('Pizza', 'ham'),
#     ('Soup', 'carrots'),
#     ('Pizza', 'cheese'),
#     ('Pizza', 'flour'),
#     ('Dessert', 'milk'),
#     ('Pizza', 'mushrooms'),
#     ('Pizza', 'tomatoes'),
#     'Stop',
# ))
#
# print(shopping_cart(
#     ('Pizza', 'ham'),
#     ('Dessert', 'milk'),
#     ('Pizza', 'ham'),
#     'Stop',
# ))
#
#
# print(shopping_cart(
#     'Stop',
#     ('Pizza', 'ham'),
#     ('Pizza', 'mushrooms'),
# ))