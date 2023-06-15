from collections import deque


def stock_availability(inventory_list, action, *other_arguments):
    inventory_list = deque(inventory_list)
    if action == "delivery":
        inventory_list.extend(other_arguments)
    elif action == "sell":
        if not other_arguments:
            inventory_list.popleft()
        else:
            parameter = other_arguments[0]
            if isinstance(parameter, int):
                for _ in range(parameter):
                    inventory_list.popleft()
            else:
                for word in other_arguments:
                    if word in inventory_list:
                        while word in inventory_list:
                            inventory_list.remove(word)

    return list(inventory_list)


print(stock_availability(["choco", "vanilla", "banana"], "delivery", "caramel", "berry"))
print(stock_availability(["chocolate", "vanilla", "banana"], "delivery", "cookie", "banana"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell", 3))
print(stock_availability(["chocolate", "chocolate", "banana"], "sell", "chocolate"))
print(stock_availability(["cookie", "chocolate", "banana"], "sell", "chocolate"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell", "cookie"))