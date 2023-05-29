from collections import deque

tasks = deque([int(x) for x in input().split(", ")])
task_idx = int(input())

clock_cycles = 0

while tasks:
    current_task = min(x for x in tasks if x != 0)
    current_task_index = tasks.index(current_task)

    if current_task_index == task_idx:
        clock_cycles += current_task
        break

    clock_cycles += current_task
    tasks[current_task_index] = 0

print(clock_cycles)