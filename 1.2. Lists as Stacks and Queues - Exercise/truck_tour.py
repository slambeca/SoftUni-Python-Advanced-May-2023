from collections import deque
pumps_data = deque([[int(x) for x in input().split()] for _ in range(int(input()))])    # [[1, 5], [10, 3], [3, 4]]

# For each element in our pumps list, at index 0 is the amount of petrol the gas station has, at index 1 is the
# distance to the next gas station

pumps_data_copy = pumps_data.copy()

index = 0    # The final result is the index
liters_in_tank = 0

while pumps_data_copy:
    petrol, distance = pumps_data_copy.popleft()    # 1, 5

    liters_in_tank += petrol

    if liters_in_tank - distance < 0:
        pumps_data.rotate(-1)    # this moves the first element to the last position in deque
        # same as pumps_data.append(pumps_data.popleft())
        pumps_data_copy = pumps_data.copy()
        index += 1
        liters_in_tank = 0
    else:
        liters_in_tank -= distance

print(index)

# 100/100 in Judge