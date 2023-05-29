from collections import deque

bomb_effects = deque(map(int, input().split(", ")))
bomb_casings = list(map(int, input().split(", ")))

datura_bombs = 0
cherry_bombs = 0
smokey_decoy_bombs = 0

is_filled = False

while bomb_effects and bomb_casings:
    first_bomb_effect = bomb_effects.popleft()
    last_bomb_casing = bomb_casings.pop()

    result = first_bomb_effect + last_bomb_casing

    if result == 40:
        datura_bombs += 1
    elif result == 60:
        cherry_bombs += 1
    elif result == 120:
        smokey_decoy_bombs += 1
    else:
        bomb_casings.append(last_bomb_casing - 5)
        bomb_effects.appendleft(first_bomb_effect)

    if datura_bombs >= 3 and cherry_bombs >= 3 and smokey_decoy_bombs >= 3:
        is_filled = True
        break

if is_filled:
    print("Bene! You have successfully filled the bomb pouch!")
else:
    print("You don't have enough materials to fill the bomb pouch.")

if bomb_effects:
    print(f"Bomb Effects: {', '.join(str(x) for x in bomb_effects)}")
else:
    print("Bomb Effects: empty")

if bomb_casings:
    print(f"Bomb Casings: {', '.join(str(x) for x in bomb_casings)}")
else:
    print("Bomb Casings: empty")

print(f"Cherry Bombs: {cherry_bombs}")
print(f"Datura Bombs: {datura_bombs}")
print(f"Smoke Decoy Bombs: {smokey_decoy_bombs}")

# Variant 2 with a dictionary
# from collections import deque
#
# bomb_effects = deque([int(x) for x in input().split(", ")])    # deque([5, 25, 25, 115])
# bomb_casings = [int(x) for x in input().split(", ")]    # [5, 15, 25, 35]
#
# filled_bomb_pouch = False
#
# bombs = {
#     "Cherry Bombs": 0,
#     "Datura Bombs": 0,
#     "Smoke Decoy Bombs": 0,
# }
#
# while bomb_effects and bomb_casings:
#     first_bomb_effect = bomb_effects.popleft()    # 5
#     last_bomb_casing = bomb_casings.pop()    # 35
#
#     their_sum = first_bomb_effect + last_bomb_casing    # 40
#
#     if their_sum == 40:
#         bombs["Datura Bombs"] += 1
#     elif their_sum == 60:
#         bombs["Cherry Bombs"] += 1
#     elif their_sum == 120:
#         bombs["Smoke Decoy Bombs"] += 1
#     else:
#         new_bomb_value = last_bomb_casing - 5
#         bomb_casings.append(new_bomb_value)
#         bomb_effects.appendleft(first_bomb_effect)
#
#     if bombs["Datura Bombs"] >= 3 and bombs["Smoke Decoy Bombs"] >= 3 and bombs["Cherry Bombs"] >= 3:
#         filled_bomb_pouch = True
#         print("Bene! You have successfully filled the bomb pouch!")
#         break
#
# if not filled_bomb_pouch:
#     print("You don't have enough materials to fill the bomb pouch.")
# if not bomb_effects:
#     print("Bomb Effects: empty")
# else:
#     print(f"Bomb Effects: {', '.join(str(x) for x in bomb_effects)}")
# if not bomb_casings:
#     print("Bomb Casings: empty")
# else:
#     print(f"Bomb Casings: {', '.join(str(x) for x in bomb_casings)}")
# for key, value in bombs.items():
#     print(f"{key}: {value}")