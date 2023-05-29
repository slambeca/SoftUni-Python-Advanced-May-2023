from collections import deque


def sum_numbers(num1, num2):
    return num1 + num2


seats = input().split(", ")    # ['17K', '20B', '3C', '15D', '31Z', '28F']

seat_matches = []

first_sequence = deque(map(int, input().split(", ")))
second_sequence = deque(map(int, input().split(", ")))

rotations = 0

while True:
    if len(seat_matches) == 3 or rotations == 10:
        break

    first_number = first_sequence.popleft()    # 20
    second_number = second_sequence.pop()    # 46

    ascii_value = chr(sum_numbers(first_number, second_number))    # B

    new_first_number_as_str = str(first_number) + ascii_value
    new_second_number_as_str = str(second_number) + ascii_value

    for seat in [new_first_number_as_str, new_second_number_as_str]:
        if seat in seat_matches:
            break
        if seat in seats:
            seat_matches.append(seat)
            seats.remove(seat)
            break
    else:
        first_sequence.append(first_number)
        second_sequence.appendleft(second_number)

    rotations += 1

print(f"Seat matches: {', '.join(seat_matches)}")
print(f"Rotations count: {rotations}")

# 100/100 in Judge