from collections import deque

pizza_orders = deque([int(x) for x in input().split(", ")])
employees = deque([int(x) for x in input().split(", ")])

total_pizzas_made = 0

while pizza_orders and employees:
    current_order = pizza_orders.popleft()

    if current_order <= 0 or current_order > 10:
        continue

    current_employee = employees.pop()

    if current_order <= current_employee:
        total_pizzas_made += current_order
        continue
    elif current_order > current_employee:
        total_pizzas_made += current_employee
        pizzas_left = current_order - current_employee
        pizza_orders.appendleft(pizzas_left)

if not pizza_orders:
    print("All orders are successfully completed!")
    print(f"Total pizzas made: {total_pizzas_made}")
    print(f"Employees: {', '.join(str(x) for x in employees)}")
if not employees:
    print("Not all orders are completed.")
    print(f"Orders left: {', '.join(str(x) for x in pizza_orders)}")
