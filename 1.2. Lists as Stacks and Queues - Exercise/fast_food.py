from collections import deque

quantity_of_food = int(input())    # 348
orders_as_deque = deque([int(x) for x in input().split()])    # deque([20, 54, 30, 16, 7, 9])

biggest_order = max(orders_as_deque)

for number in range(len(orders_as_deque)):    # for order in orders.copy()
    order = orders_as_deque[0]
    if quantity_of_food - order >= 0:
        quantity_of_food -= int(order)
        orders_as_deque.popleft()
    else:
        break

print(biggest_order)

if not orders_as_deque:
    print(f"Orders complete")
else:
    print(f"Orders left: ", end="")
    for number in orders_as_deque:    # ' '.join[str(o) for o in orders_as_deque]
        print(number, end=" ")
