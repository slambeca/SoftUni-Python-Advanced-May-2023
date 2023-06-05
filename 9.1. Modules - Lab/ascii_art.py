from pyfiglet import figlet_format


def print_func(message):
    return figlet_format(message)


print(print_func(input()))

