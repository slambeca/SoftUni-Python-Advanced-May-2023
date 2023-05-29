from collections import deque

bowls_ramen = list(map(int, input().split(", ")))
customers = deque(map(int, input().split(", ")))

while bowls_ramen and customers:
    current_bowl = bowls_ramen.pop()    # 19
    current_customer = customers.popleft()    # 58

    if current_bowl == current_customer:
        continue
    elif current_bowl > current_customer:
        current_bowl -= current_customer
        bowls_ramen.append(current_bowl)
    else:
        current_customer -= current_bowl
        customers.appendleft(current_customer)

if not customers and not bowls_ramen:
    print("Great job! You served all the customers.")
elif not customers:
    print(f"Great job! You served all the customers.")
    print(f"Bowls of ramen left: {', '.join(str(x) for x in bowls_ramen)}")
elif not bowls_ramen:
    print(f"Out of ramen! You didn't manage to serve all customers.")
    print(f"Customers left: {', '.join(str(x) for x in customers)}")

# Variant 2
from collections import deque

bowls_of_ramen = [int(x) for x in input().split(", ")]
customers = deque([int(x) for x in input().split(", ")])

while bowls_of_ramen and customers:
    current_bow_of_ramen = bowls_of_ramen[-1]
    current_customer = customers[0]

    if current_bow_of_ramen == current_customer:
        bowls_of_ramen.pop()
        customers.popleft()
    elif current_bow_of_ramen > current_customer:
        current_bow_of_ramen -= current_customer
        customers.popleft()
        bowls_of_ramen[-1] = current_bow_of_ramen
    elif current_customer > current_bow_of_ramen:
        bowls_of_ramen.pop()
        current_customer -= current_bow_of_ramen
        customers[0] = current_customer

if not customers:
    print("Great job! You served all the customers.")
    if bowls_of_ramen:
        print(f"Bowls of ramen left: {', '.join((str(x) for x in bowls_of_ramen))}")
else:
    print("Out of ramen! You didn't manage to serve all customers.")
    print(f"Customers left: {', '.join(str(x) for x in customers)}")