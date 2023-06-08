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
    
# # Variant 2
# from collections import deque
# 
# elves = deque([int(x) for x in input().split()])
# materials = deque([int(x) for x in input().split()])
# 
# total_energy = 0
# total_toys = 0
# iterations = 0
# 
# while elves and materials:
#     elf = elves.popleft()
#     material = materials[-1]
# 
#     if elf < 5:
#         continue
# 
#     iterations += 1
#     current_toys_count = 0
# 
#     if iterations % 3 == 0:
#         material *= 2
#         current_toys_count += 1
# 
#     if elf >= material:
#         total_energy += material
#         elf -= material
# 
#         if iterations % 5 != 0:
#             elf += 1
#             current_toys_count += 1
#         else:
#             current_toys_count = 0
# 
#         materials.pop()
#     else:
#         elf *= 2
#         current_toys_count = 0
# 
#     total_toys += current_toys_count
# 
#     elves.append(elf)
# 
# print(f"Toys: {total_toys}\nEnergy: {total_energy}")
# if elves:
#     print(f"Elves left: {', '.join(str(x) for x in elves)}")
# if materials:
#     print(f"Boxes left: {', '.join(str(x) for x in materials)}")
