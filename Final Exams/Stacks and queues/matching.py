from collections import deque

males = list(map(int, input().split()))
females = deque(map(int, input().split()))

matches = 0

while males and females:
    current_female = females[0]
    current_male = males[-1]

    if current_female % 25 == 0:
        females.popleft()
        continue
    elif current_male % 25 == 0:
        males.pop()
        continue

    if current_female <= 0:
        females.popleft()
        continue
    elif current_male <= 0:
        males.pop()
        continue

    if current_female == current_male:
        females.popleft()
        males.pop()
        matches += 1
    else:
        females.popleft()
        current_male -= 2
        males[-1] = current_male

print(f"Matches: {matches}")
if males:
    males.reverse()
    print(f"Males left: {', '.join(str(x) for x in males)}")
else:
    print(f"Males left: none")
if females:
    print(f"Females left: {', '.join(str(x) for x in females)}")
else:
    print(f"Females left: none")

# Variant 2
# from collections import deque
#
# males = [int(x) for x in input().split()]
# females = deque([int(x) for x in input().split()])
#
# matches = 0
#
# while males and females:
#     current_male = males[-1]
#     current_female = females[0]
#
#     if current_male % 25 == 0 and current_male != 0:
#         males.pop()
#         males.pop()
#         continue
#     elif current_female % 25 == 0 and current_female != 0:
#         females.popleft()
#         females.popleft()
#         continue
#
#     if current_male <= 0:
#         males.pop()
#         continue
#     elif current_female <= 0:
#         females.popleft()
#         continue
#
#     if current_male == current_female:
#         males.pop()
#         females.popleft()
#         matches += 1
#     else:
#         females.popleft()
#         males[-1] -= 2
#
# print(f"Matches: {matches}")
# if males:
#     print(f"Males left: {', '.join(str(x) for x in males[::-1])}")
# else:
#     print("Males left: none")
# if females:
#     print(f"Females left: {', '.join(str(x) for x in females)}")
# else:
#     print("Females left: none")

# Variant 3
# from collections import deque
# 
# males = deque([int(x) for x in input().split()])
# females = deque([int(x) for x in input().split()])
# 
# matches = 0
# 
# while males and females:
#     current_female = females.popleft()
#     current_male = males.pop()
# 
#     if current_female <= 0:
#         males.append(current_male)
#         continue
# 
#     if current_male <= 0:
#         females.appendleft(current_female)
#         continue
# 
#     if current_male % 25 == 0:
#         males.pop()
#         females.appendleft(current_female)
#         continue
#     elif current_female % 25 == 0:
#         females.popleft()
#         males.append(current_male)
#         continue
# 
#     if current_male == current_female:
#         matches += 1
#         continue
#     else:
#         current_male -= 2
#         males.append(current_male)
# 
# print(f"Matches: {matches}")
# if males:
#     males.reverse()
#     print(f"Males left: {', '.join(str(x) for x in males)}")
# else:
#     print(f"Males left: none")
# 
# if females:
#     print(f"Females left: {', '.join(str(x) for x in females)}")
# else:
#     print("Females left: none")
