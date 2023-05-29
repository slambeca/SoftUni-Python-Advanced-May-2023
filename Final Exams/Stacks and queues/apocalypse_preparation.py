from collections import deque

healing_items = {
    "Patch": 0,
    "Bandage": 0,
    "MedKit": 0
}

PATCH = 30
BANDAGE = 40
MEDKIT = 100

textiles = deque([int(x) for x in input().split()])    # deque([20, 10, 40, 70, 20])
medicaments = list(map(int, input().split()))    # [10, 50, 10, 30, 20, 80]

while True:
    if not textiles and not medicaments:
        print(f"Textiles and medicaments are both empty.")
        break
    elif not textiles:
        print(f"Textiles are empty.")
        break
    elif not medicaments:
        print(f"Medicaments are empty.")
        break

    first_textile = textiles.popleft()
    last_medicament = medicaments.pop()

    sum_values = first_textile + last_medicament

    if sum_values == PATCH:
        healing_items["Patch"] += 1
    elif sum_values == BANDAGE:
        healing_items["Bandage"] += 1
    elif sum_values == MEDKIT:
        healing_items["MedKit"] += 1
    elif sum_values > MEDKIT:
        healing_items["MedKit"] += 1
        medicaments[-1] += sum_values - MEDKIT
    else:
        medicaments.append(last_medicament + 10)

healing_items = sorted(healing_items.items(), key=lambda x: (-x[1], x[0]))

for key, value in healing_items:
    if int(value) > 0:    # If any items, 0 is not accepted
        print(f"{key} - {value}")

if medicaments:
    medicaments.reverse()
    print(f"Medicaments left: {', '.join(str(x) for x in medicaments)}")
if textiles:
    print(f"Textiles left: {', '.join(str(x) for x in textiles)}")

# Variant 2
# from collections import deque
#
# textiles = deque([int(x) for x in input().split()])    # deque([20, 10, 40, 70, 20])
# medicaments = [int(x) for x in input().split()]    # [10, 50, 10, 30, 20, 80]
#
# healing_items = {
#     "Patch": 0,
#     "Bandage": 0,
#     "MedKit": 0
# }
#
# while textiles and medicaments:
#     first_textile = textiles.popleft()    # 20
#     last_medicament = medicaments.pop()    # 80
#
#     their_sum = first_textile + last_medicament    # 100
#
#     if their_sum == 30:
#         healing_items["Patch"] += 1
#     elif their_sum == 40:
#         healing_items["Bandage"] += 1
#     elif their_sum == 100:
#         healing_items["MedKit"] += 1
#     elif their_sum > 100:
#         healing_items["MedKit"] += 1
#         remaining_value = their_sum - 100    # 10
#         medicaments[-1] += remaining_value
#     else:
#         medicaments.append(last_medicament + 10)
#
# healing_items = dict(sorted(healing_items.items(), key=lambda x: (-x[1], x[0])))
#
# if not medicaments and not textiles:
#     print("Textiles and medicaments are both empty.")
#     for key, value in healing_items.items():
#         if int(value) > 0:
#             print(f"{key} - {value}")
# elif not textiles:
#     print("Textiles are empty.")
#     for key, value in healing_items.items():
#         if int(value) > 0:
#             print(f"{key} - {value}")
#     print(f"Medicaments left: {', '.join(str(x) for x in medicaments[::-1])}")
# elif not medicaments:
#     print("Medicaments are empty.")
#     for key, value in healing_items.items():
#         if int(value) > 0:
#             print(f"{key} - {value}")
#     print(f"Textiles left: {', '.join(str(x) for x in textiles)}")