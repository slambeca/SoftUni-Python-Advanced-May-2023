from collections import deque

firework_effects = deque([int(x) for x in input().split(", ")])
explosive_power = [int(x) for x in input().split(", ")]

palm_fireworks = 0
willow_fireworks = 0
crossette_fireworks = 0

perfect_show = False

while firework_effects and explosive_power:
    current_firework_effect = firework_effects[0]
    current_explosive_fire = explosive_power[-1]

    if current_firework_effect <= 0:
        firework_effects.popleft()
        continue
    elif current_explosive_fire <= 0:
        explosive_power.pop()
        continue

    their_sum = current_firework_effect + current_explosive_fire

    if their_sum % 15 == 0:
        crossette_fireworks += 1
        firework_effects.popleft()
        explosive_power.pop()
        if palm_fireworks >= 3 and crossette_fireworks >= 3 and willow_fireworks >= 3:
            perfect_show = True
            break
        continue
    elif their_sum % 5 == 0 and their_sum % 3 != 0:
        willow_fireworks += 1
        firework_effects.popleft()
        explosive_power.pop()
        if palm_fireworks >= 3 and crossette_fireworks >= 3 and willow_fireworks >= 3:
            perfect_show = True
            break
        continue
    elif their_sum % 3 == 0 and their_sum % 5 != 0:
        palm_fireworks += 1
        firework_effects.popleft()
        explosive_power.pop()
        if palm_fireworks >= 3 and crossette_fireworks >= 3 and willow_fireworks >= 3:
            perfect_show = True
            break
        continue
    else:
        decreased_value = (firework_effects.popleft() - 1)
        firework_effects.append(decreased_value)

if perfect_show:
    print("Congrats! You made the perfect firework show!")
else:
    print("Sorry. You can't make the perfect firework show.")
if firework_effects:
    print(f"Firework Effects left: {', '.join(str(x) for x in firework_effects)}")
if explosive_power:
    print(f"Explosive Power left: {', '.join(str(x) for x in explosive_power)}")

print(f"Palm Fireworks: {palm_fireworks}\nWillow Fireworks: {willow_fireworks}\n"
      f"Crossette Fireworks: {crossette_fireworks}")