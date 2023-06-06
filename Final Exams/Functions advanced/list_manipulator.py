from collections import deque


def list_manipulator(numbers, *args):
    action, position, *new_numbers = args

    numbers = deque(numbers)

    if action == "remove":
        if position == "beginning":
            if new_numbers:
                iterations = new_numbers[0]
                for _ in range(iterations):
                    numbers.popleft()
            else:
                numbers.popleft()
        else:
            if new_numbers:
                iterations = new_numbers[0]
                for _ in range(iterations):
                    numbers.pop()
            else:
                numbers.pop()

    elif action == "add":
        if position == "beginning":
            for number in new_numbers[::-1]:
                numbers.appendleft(number)
        else:
            numbers.extend(new_numbers)

    return list(numbers)


# print(list_manipulator([1,2,3], "remove", "end"))
# print(list_manipulator([1,2,3], "remove", "beginning"))
# print(list_manipulator([1,2,3], "add", "beginning", 20))
# print(list_manipulator([1,2,3], "add", "end", 30))
# print(list_manipulator([1,2,3], "remove", "end", 2))
# print(list_manipulator([1,2,3], "remove", "beginning", 2))
# print(list_manipulator([1,2,3], "add", "beginning", 20, 30, 40))
# print(list_manipulator([1,2,3], "add", "end", 30, 40, 50))
