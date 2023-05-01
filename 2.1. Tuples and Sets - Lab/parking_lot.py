count_cars = int(input())

registrations = set()

COMMAND_IN = "IN"
COMMAND_OUT = "OUT"

for _ in range(count_cars):
    command = input()

    command_args = command.split(", ")

    action = command_args[0]
    registration = command_args[1]

    if action == COMMAND_IN:
        registrations.add(registration)
    elif action == COMMAND_OUT:
        registrations.remove(registration)

if registrations:
    print("\n".join(registrations))
else:
    print("Parking Lot is Empty")

# # Variant 2
#
#
# def print_func(data):
#     if data:
#         print("\n".join(data))
#         return
#     print(f"Parking Lot is Empty")
#
#
# n = int(input())
#
# plate_number_records = [input() for _ in range(n)]
#
# parking_lot_data = set()
#
# COMMAND_IN = "IN"
# COMMAND_OUT = "OUT"
#
# for record in plate_number_records:
#     command, registration = record.split(", ")
#
#     if command == COMMAND_IN:
#         parking_lot_data.add(registration)
#     elif command == COMMAND_OUT:
#         parking_lot_data.remove(registration)
#
# print_func(parking_lot_data)