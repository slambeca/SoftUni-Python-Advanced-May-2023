from custom_module_3 import create_sequence, locate

while True:
    command = input()

    if command == "Stop":
        break

    command_args = command.split()

    action = command_args[0]
    value = int(command_args[-1])

    if action == "Create":
        print(create_sequence(value))
    elif action == "Locate":
        print(locate(value))