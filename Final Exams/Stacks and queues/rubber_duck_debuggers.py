from collections import deque

time_per_task = deque([int(x) for x in input().split()])    # deque([10, 15, 12, 18, 22, 6])
number_of_tasks = [int(x) for x in input().split()]    # [12, 16, 5, 6, 9, 1]

dictionary = {
    "Darth Vader Ducky": 0,
    "Thor Ducky": 0,
    "Big Blue Rubber Ducky": 0,
    "Small Yellow Rubber Ducky": 0
}

while time_per_task and number_of_tasks:
    current_time_per_task = time_per_task.popleft()    # 10
    current_number_of_tasks = number_of_tasks.pop()    # 1

    result = current_time_per_task * current_number_of_tasks    # 10

    if 0 <= result <= 60:
        dictionary["Darth Vader Ducky"] += 1
    elif 61 <= result <= 120:
        dictionary["Thor Ducky"] += 1
    elif 121 <= result <= 180:
        dictionary["Big Blue Rubber Ducky"] += 1
    elif 181 <= result <= 240:
        dictionary["Small Yellow Rubber Ducky"] += 1
    elif result > 240:
        current_number_of_tasks -= 2
        number_of_tasks.append(current_number_of_tasks)
        time_per_task.append(current_time_per_task)

print(f"Congratulations, all tasks have been completed! Rubber ducks rewarded:")
for key, value in dictionary.items():
    print(f"{key}: {value}")
    
# Variant 2
# from collections import deque
# 
# times_for_a_task = deque([int(x) for x in input().split()])
# number_of_tasks = deque([int(x) for x in input().split()])
# 
# darth_vader_ducky, thor_ducky, big_blue_rubber_ducky, small_yellow_rubber_ducky = 0, 0, 0, 0
# 
# while times_for_a_task and number_of_tasks:
#     current_time = times_for_a_task.popleft()
#     current_task = number_of_tasks.pop()
# 
#     result = current_time * current_task
# 
#     if 0 <= result <= 60:
#         darth_vader_ducky += 1
#     elif 61 <= result <= 120:
#         thor_ducky += 1
#     elif 121 <= result <= 180:
#         big_blue_rubber_ducky += 1
#     elif 181 <= result <= 240:
#         small_yellow_rubber_ducky += 1
#     else:
#         times_for_a_task.append(current_time)
#         number_of_tasks.append(current_task - 2)
# 
# print("Congratulations, all tasks have been completed! Rubber ducks rewarded:")
# print(f"Darth Vader Ducky: {darth_vader_ducky}\nThor Ducky: {thor_ducky}\nBig Blue Rubber Ducky: {big_blue_rubber_ducky}\n"
#       f"Small Yellow Rubber Ducky: {small_yellow_rubber_ducky}")
