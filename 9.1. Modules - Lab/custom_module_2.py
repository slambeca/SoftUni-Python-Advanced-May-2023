# This custom module is for exercise 4.mathematical_operations


def mathematical_operations(received_string):
    received_string_args = received_string.split()

    num_one = float(received_string_args[0])
    sign = received_string_args[1]
    num_two = int(received_string_args[2])

    result = 0

    if sign == "/":
        result = num_one / num_two
    elif sign == "*":
        result = num_one * num_two
    elif sign == "-":
        result = num_one - num_two
    elif sign == "+":
        result = num_one + num_two
    elif sign == "^":
        result = num_one ** num_two
    else:
        raise Exception(f"Invalid sign {sign}")

    return f"{result:.2f}"