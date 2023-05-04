def operate(operator, *args):
    result = args[0]
    if operator == "+":
        result = sum(args)
    elif operator == "-":
        for num in args[1:]:
            result -= num
    elif operator == "*":
        for num in args[1:]:
            result *= num
    elif operator == "/":
        for num in args[1:]:
            result /= num

    return result