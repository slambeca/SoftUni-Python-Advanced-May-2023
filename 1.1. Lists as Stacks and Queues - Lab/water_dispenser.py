from collections import deque

COMMAND_START: str = "Start"
COMMAND_END: str = "End"
COMMAND_REFILL: str = "refill"

my_queue = deque()

water_quantity: int = int(input())

while True:
    name: str = input()

    if name == COMMAND_START:
        break

    my_queue.append(name)

while True:
    command: str = input()

    if command == COMMAND_END:
        print(f"{water_quantity} liters left")
        break

    if command.startswith(COMMAND_REFILL):
        splitted_command = command.split()
        added_liters: int = int(splitted_command[1])
        water_quantity += added_liters
    else:
        removed_litters = int(command)
        if water_quantity - removed_litters >= 0:
            water_quantity -= removed_litters
            print(f"{my_queue.popleft()} got water")
        else:
            print(f"{my_queue.popleft()} must wait")