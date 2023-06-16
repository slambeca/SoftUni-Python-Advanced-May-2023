def shop_from_grocery_list(budget, grocery_list, *products):
    remaining_budget = budget

    for item in products:
        product = item[0]
        price = item[1]

        if not remaining_budget >= price:
            break

        if product in grocery_list:
            remaining_budget -= price
            grocery_list.remove(product)

    if not grocery_list:
        return f"Shopping is successful. Remaining budget: {remaining_budget:.2f}."

    return f"You did not buy all the products. Missing products: {', '.join(grocery_list)}."


print(shop_from_grocery_list(
    100,
    ["tomato", "cola"],
    ("cola", 5.8),
    ("tomato", 10.0),
    ("tomato", 20.45),
))

print(shop_from_grocery_list(
    100,
    ["tomato", "cola", "chips", "meat"],
    ("cola", 5.8),
    ("tomato", 10.0),
    ("meat", 22),
))

print(shop_from_grocery_list(
    100,
    ["tomato", "cola", "chips", "meat", "chocolate"],
    ("cola", 15.8),
    ("chocolate", 30),
    ("tomato", 15.85),
    ("chips", 50),
    ("meat", 22.99),
))

# Variant 2
# def shop_from_grocery_list(budget, grocery_list, *products):
#     purchased_products = []
#     remaining_budget = budget
#
#     for product in products:
#         product_name, product_price = product
#
#         if product_name not in grocery_list:
#             continue
#
#         if product_name in purchased_products:
#             continue
#
#         if remaining_budget < product_price:
#             break
#
#         purchased_products.append(product_name)
#         remaining_budget -= product_price
#
#     if set(purchased_products) == set(grocery_list):
#         return f"Shopping is successful. Remaining budget: {remaining_budget:.2f}."
#     else:
#         missing_products = set(grocery_list) - set(purchased_products)
#         return f"You did not buy all the products. Missing products: {', '.join(missing_products)}."