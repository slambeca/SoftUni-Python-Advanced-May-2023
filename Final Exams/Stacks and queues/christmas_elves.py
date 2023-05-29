from collections import deque

energy = deque([int(x) for x in input().split()])    # deque([10, 16, 13, 25])
materials = [int(x) for x in input().split()]    # [12, 11, 8]

toys_made = 0
total_energy_used = 0
rotations = 1

while energy and materials:
    current_energy = energy.popleft()    # 10

    if current_energy < 5:
        continue

    current_material = materials.pop()    # 8

    if current_energy >= current_material:
        if rotations % 3 != 0:
            toys_made += 1
            if rotations % 5 == 0:
                toys_made -= 1
                energy.append(current_energy - current_material)
                total_energy_used += current_material
                rotations += 1
                continue
            total_energy_used += current_material
            energy.append((current_energy - current_material) + 1)
        elif rotations % 3 == 0:
            if current_energy >= current_material * 2:
                toys_made += 2
                if rotations % 5 == 0:
                    toys_made -= 2
                    energy.append(current_energy - (current_material * 2))
                    rotations += 1
                    total_energy_used += current_material * 2
                    continue
                energy.append(current_energy - (current_material * 2) + 1)
                total_energy_used += current_material * 2
            else:
                materials.append(current_material)
                energy.append(current_energy * 2)
    else:
        materials.append(current_material)
        energy.append(current_energy * 2)

    rotations += 1

print(f"Toys: {toys_made}")
print(f"Energy: {total_energy_used}")
if energy:
    print(f"Elves left: {', '.join(str(x) for x in energy)}")
if materials:
    print(f"Boxes left: {', '.join(str(x) for x in materials)}")