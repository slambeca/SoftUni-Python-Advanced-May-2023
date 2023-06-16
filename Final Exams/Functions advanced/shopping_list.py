LIMIT = 5


def shopping_list(budget, **kwargs):
    bought_products = 0
    result = ""

    if not budget >= 100:
        return "You do not have enough budget."
    else:
        for key, values in kwargs.items():
            if budget >= values[0] * values[1]:
                budget -= values[0] * values[1]
                bought_products += 1
                result += f"You bought {key} for {values[0] * values[1]:.2f} leva.\n"
                if bought_products == LIMIT:
                    break

    return result.strip()


print(shopping_list(100,
                    microwave=(70, 2),
                    skirts=(15, 4),
                    coffee=(1.50, 10),
                    ))


print(shopping_list(20,
                    jeans=(19.99, 1),
                    ))

print(shopping_list(104,
                    cola=(1.20, 2),
                    candies=(0.25, 15),
                    bread=(1.80, 1),
                    pie=(10.50, 5),
                    tomatoes=(4.20, 1),
                    milk=(2.50, 2),
                    juice=(2, 3),
                    eggs=(3, 1),
                    ))