from collections import deque

queue = deque()

COMMAND_END = "End"
COMMAND_PAID = "Paid"

people_in_queue = 0

while True:
    customer = input()

    if customer == COMMAND_END:
        break

    if customer == COMMAND_PAID:
        for i in range(people_in_queue):
            print(queue.popleft())
            people_in_queue -= 1
        continue

    queue.append(customer)
    people_in_queue += 1

print(f"{len(queue)} people remaining.")

# # Variant 2
# people = []
#
# while True:
#     command = input()
#
#     if command == "End":
#         break
#
#     if command == "Paid":
#         for i in range(len(people)):
#             print(people.pop(0))
#         continue
#
#     people.append(command)
#
# print(f"{len(people)} people remaining.")
#
# # Variant 3
# from collections import deque
#
# names_deque = deque()
#
# COMMAND_END: str = "End"
# COMMAND_PAID: str = "Paid"
#
# while True:
#     command = input()
#
#     if command == COMMAND_END:
#         print(f"{len(names_deque)} people remaining.")
#         break
#
#     elif command == COMMAND_PAID:
#         while names_deque:
#             print(names_deque.popleft())
#
#     else:
#         names_deque.append(command)