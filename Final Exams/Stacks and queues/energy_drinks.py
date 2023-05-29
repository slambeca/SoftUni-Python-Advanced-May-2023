from collections import deque

# 0.030s with list comprehension, 0.040s with map
milligrams_of_caffeine = list(map(int, input().split(", ")))
energy_drinks = deque(map(int, input().split(", ")))

MAXIMUM_CAFFEINE = 300

total_caffeine = 0

while milligrams_of_caffeine and energy_drinks:
    last_caffeine = milligrams_of_caffeine.pop()
    first_energy_drink = energy_drinks.popleft()

    result = last_caffeine * first_energy_drink

    if total_caffeine + result <= MAXIMUM_CAFFEINE:
        total_caffeine += result
    else:
        energy_drinks.append(first_energy_drink)
        total_caffeine -= 30
        if total_caffeine <= 0:
            total_caffeine = 0

if energy_drinks:
    print(f"Drinks left: {', '.join(str(x) for x in energy_drinks)}")
else:
    print("At least Stamat wasn't exceeding the maximum caffeine.")

print(f"Stamat is going to sleep with {total_caffeine } mg caffeine.")