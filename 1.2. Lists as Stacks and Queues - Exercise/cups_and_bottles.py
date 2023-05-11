from collections import deque

cups_capacity = deque([int(x) for x in input().split()])    
bottles_capacity = [int(x) for x in input().split()]    

wasted_water_lts = 0

while cups_capacity and bottles_capacity:
    current_bottle = bottles_capacity.pop()   
    current_cup = cups_capacity.popleft()    

    if current_bottle >= current_cup:
        current_bottle -= current_cup
        if current_bottle >= 0:
            wasted_water_lts += current_bottle
    elif current_bottle < current_cup:
        current_cup -= current_bottle
        if current_cup <= 0:
            continue
        else:
            cups_capacity.appendleft(current_cup)

if bottles_capacity:
    print(f"Bottles: {' '.join(str(x) for x in bottles_capacity)}")
if cups_capacity:
    print(f"Cups: {' '.join(str(x) for x in cups_capacity)}")
print(f"Wasted litters of water: {wasted_water_lts}")
