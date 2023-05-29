from collections import deque

materials = deque(map(int, input().split()))
magic_level = deque(map(int, input().split()))

presents = []

while materials and magic_level:
    current_material = materials.pop()
    current_magic = magic_level.popleft()

    result = current_material + current_magic

    if 400 <= result <= 499:
        presents.append("Diamond Jewellery")
        continue
    elif 300 <= result <= 399:
        presents.append("Gold")
        continue
    elif 200 <= result <= 299:
        presents.append("Porcelain Sculpture")
        continue
    elif 100 <= result <= 199:
        presents.append("Gemstone")
        continue

    if result > 499:
        result /= 2
        if 400 <= result <= 499:
            presents.append("Diamond Jewellery")
        elif 300 <= result <= 399:
            presents.append("Gold")
        elif 200 <= result <= 299:
            presents.append("Porcelain Sculpture")
        elif 100 <= result <= 199:
            presents.append("Gemstone")

    elif result < 100:
        if result % 2 == 0:
            materials.append(current_material * 2)
            magic_level.appendleft(current_magic * 3)
            continue
        else:
            result = (current_material + current_magic) * 2
            if 400 <= result <= 499:
                presents.append("Diamond Jewellery")
            elif 300 <= result <= 399:
                presents.append("Gold")
            elif 200 <= result <= 299:
                presents.append("Porcelain Sculpture")
            elif 100 <= result <= 199:
                presents.append("Gemstone")

if {"Gold", "Diamond Jewellery"}.issubset(presents) or {"Gemstone", "Porcelain Sculpture"}.issubset(presents):
    print("The wedding presents are made!")
else:
    print("Aladdin does not have enough wedding presents.")

if materials:
    print(f"Materials left: {', '.join(str(x) for x in materials)}")
if magic_level:
    print(f"Magic left: {', '.join(str(x) for x in magic_level)}")

[print(f"{toy}: {presents.count(toy)}") for toy in sorted(set(presents))]