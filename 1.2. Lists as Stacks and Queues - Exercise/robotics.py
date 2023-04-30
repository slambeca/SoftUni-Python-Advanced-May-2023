from collections import deque
from datetime import datetime, timedelta

COMMAND_END = "End"

# {name: [time_for_one_task, 0]} 0 means the robot is free
robots = {robot.split("-")[0]: [int(robot.split("-")[1]), 0] for robot in input().split(";")}
# {'ROB': [15, 0], 'SS2': [10, 0], 'NX8000': [3, 0]}

factory_time = datetime.strptime(input(), "%H:%M:%S")    # 8:00:00

products = deque()    # deque(['detail', 'glass', 'wood', 'apple'])

while True:
    product = input()

    if product == COMMAND_END:
        break

    products.append(product)

while products:
    factory_time += timedelta(0, 1)    # 0 is for days, 1 is for seconds
    product = products.popleft()

    robots = {r[0]: [r[1][0], r[1][1] - 1] if r[1][1] != 0 else r[1] for r in robots.items()}

    free_robots = list(filter(lambda x: x[1][1] == 0, robots.items()))

    if not free_robots:
        products.append(product)
        continue

    robots[free_robots[0][0]][1] = free_robots[0][1][0]

    print(f"{free_robots[0][0]} - {product} [{factory_time.strftime('%H:%M:%S')}]")

# 100/100 in Judge

# Variant 2
from collections import deque
from datetime import datetime, timedelta

COMMAND_END = "End"

robots = {}

for robot in input().split(";"):
    name, time_needed = robot.split("-")
    robots[name] = [int(time_needed), 0]

factory_time = datetime.strptime(input(), "%H:%M:%S")    # 8:00:00

products = deque()    # deque(['detail', 'glass', 'wood', 'apple'])

while True:
    product = input()

    if product == COMMAND_END:
        break

    products.append(product)

while products:
    factory_time += timedelta(0, 1)    # 0 is for days, 1 is for seconds
    product = products.popleft()

    free_robots = []

    for name, value in robots.items():
        if value[1] != 0:
            robots[name][1] -= 1

    for name, value in robots.items():
        if value[1] == 0:
            free_robots.append([name, value])

    if not free_robots:
        products.append(product)
        continue

    robot_name, data = free_robots[0]
    robots[robot_name][1] = data[0]

    print(f"{free_robots[0][0]} - {product} [{factory_time.strftime('%H:%M:%S')}]")

# 100/100 in Judge