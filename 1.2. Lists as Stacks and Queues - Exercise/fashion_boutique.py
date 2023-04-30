from collections import deque

clothes = deque([int(x) for x in input().split()])    # deque([5, 4, 8, 6, 3, 8, 7, 7, 9])

rack_capacity = int(input())

clothes.reverse()    # deque([9, 7, 7, 8, 3, 6, 8, 4, 5])

current_sum = 0
used_racks = 0

for item in clothes.copy():
    if current_sum + item <= rack_capacity:
        current_sum += item
        clothes.popleft()
        if current_sum == rack_capacity:
            used_racks += 1
            current_sum = 0
    else:
        used_racks += 1
        current_sum = item
        clothes.popleft()

if current_sum:
    used_racks += 1

print(used_racks)

# 100/100 in Judge

# Variant 2
clothes = [int(x) for x in input().split()]
rack_space = int(input())

racks_count = 1
current_rack_space = rack_space

while clothes:
    item_value = clothes.pop()

    if current_rack_space - item_value >= 0:
        current_rack_space -= item_value
    else:
        racks_count += 1
        current_rack_space = rack_space - item_value

print(racks_count)

# 100/100 in Judge