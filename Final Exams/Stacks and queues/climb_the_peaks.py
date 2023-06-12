from collections import deque

conquered_peaks = []

all_peaks = deque([
    ("Vihren", 80),
    ("Kutelo", 90),
    ("Banski Suhodol", 100),
    ("Polezhan", 60),
    ("Kamenitza", 70)
])

day = 1

food_portions = list(map(int, input().split(", ")))  # [40, 40, 40, 40, 40, 40, 40]
daily_stamina = deque(map(int, input().split(", ")))  # deque([40, 50, 60, 20, 30, 5, 2])

while True:
    if len(conquered_peaks) == 5:
        print(f"Alex did it! He climbed all top five Pirin peaks in one week -> @FIVEinAWEEK")
        break
    elif day > 7 or not food_portions or not daily_stamina:
        print(f"Alex failed! He has to organize his journey better next time -> @PIRINWINS")
        break

    food = food_portions.pop()  # 40
    stamina = daily_stamina.popleft()  # 40

    result = food + stamina  # 80

    current_peak = all_peaks.popleft()  # ["Vihren", 80]

    if result >= current_peak[1]:
        conquered_peaks.append(current_peak[0])
    else:
        all_peaks.appendleft(current_peak)

    day += 1

if conquered_peaks:
    print(f"Conquered peaks:")
    for peak in conquered_peaks:
        print(peak)
        
# Variant 2
# from collections import deque
# 
# conquered_peaks = []
# day = 1
# 
# all_peaks = deque([
#     ("Vihren", 80),
#     ("Kutelo", 90),
#     ("Banski Suhodol", 100),
#     ("Polezhan", 60),
#     ("Kamenitza", 70)
# ])
# 
# daily_portions = deque([int(x) for x in input().split(", ")])
# daily_stamina = deque([int(x) for x in input().split(", ")])
# 
# while True:
#     if len(conquered_peaks) == 5:
#         print("Alex did it! He climbed all top five Pirin peaks in one week -> @FIVEinAWEEK")
#         break
# 
#     if day > 7 or not daily_portions or not daily_stamina:
#         print("Alex failed! He has to organize his journey better next time -> @PIRINWINS")
#         break
# 
#     current_daily_portion = daily_portions.pop()
#     current_daily_stamina = daily_stamina.popleft()
# 
#     result = current_daily_portion + current_daily_stamina
# 
#     if result >= all_peaks[0][1]:
#         conquered_peaks.append(all_peaks[0][0])
#         all_peaks.popleft()
#         day += 1
# 
# if conquered_peaks:
#     print("Conquered peaks:")
#     for peak in conquered_peaks:
#         print(peak)
