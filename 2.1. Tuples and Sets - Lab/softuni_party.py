count_reservations = int(input())

COMMAND_END = "END"

regular_guests_list = set()    # {'SVQXQCbc', 'Ce8vwPmE'}
vip_guests_list = set()    # {'9NoBUajQ'}

all_guests = set()

reservation_codes = set([input() for code in range(count_reservations)])
# {'7IK9Yo0h', 'Ce8vwPmE', '9NoBUajQ', 'tSzE5t0p', 'SVQXQCbc'}

while True:
    guest = input()

    if guest == COMMAND_END:
        break

    elif guest in reservation_codes:
        if guest[0].isdigit():
            vip_guests_list.add(guest)
        else:
            regular_guests_list.add(guest)
        all_guests.add(guest)
    else:
        continue

print(len(reservation_codes) - (len(regular_guests_list) + len(vip_guests_list)))    # 2

missing_guests = reservation_codes.difference(all_guests)

print('\n'.join(sorted(missing_guests)))

# # Variant 2
#
#
# def collect_data_for_arrived_guests():
#     arrived_guests_list = []
#     while True:
#         data = input()
#
#         if data == "END":
#             break
#         else:
#             arrived_guests_list.append(data)
#
#     return arrived_guests_list
#
#
# def print_func(not_arrived_guests_data):
#     print(len(not_arrived_guests_data))
#     for guest_number in sorted(not_arrived_guests_data):
#         print(guest_number)
#
#
# n = int(input())
#
# guest_reservations_list = [input() for _ in range(n)]
#
# arrived_guests = collect_data_for_arrived_guests()
#
# not_arrived_guests = set(guest_reservations_list).difference(arrived_guests)
#
# print_func(not_arrived_guests)