# This is exam-like exercise
from collections import deque

chocolates = deque([int(x) for x in input().split(", ")])    # [20, 24, -5, 17, 22, 60, 26]
cups_of_milk = deque([int(x) for x in input().split(", ")])    # [26, 60, 22, 17, 24, 10, 55]

milkshakes = 0

while milkshakes != 5 and cups_of_milk and chocolates:
    chocolate = chocolates.pop()    # 26
    cup_of_milk = cups_of_milk.popleft()    # 26

    if chocolate <= 0 and cup_of_milk <= 0:
        continue
    elif chocolate <= 0:
        cups_of_milk.appendleft(cup_of_milk)
        continue
    elif cup_of_milk <= 0:
        chocolates.append(chocolate)
        continue

    if chocolate == cup_of_milk:
        milkshakes += 1
    else:
        cups_of_milk.append(cup_of_milk)    # Move the cup of milk at the end of the sequence
        chocolates.append(chocolate - 5)    # Decrease the value of the chocolate with 5, don`t change it`s position

if milkshakes == 5:
    print(f"Great! You made all the chocolate milkshakes needed!")
else:
    print(f"Not enough milkshakes.")

print(f"Chocolate: {', '.join(str(x) for x in chocolates) or 'empty'}")
print(f"Milk: {', '.join(str(x) for x in cups_of_milk) or 'empty'}")