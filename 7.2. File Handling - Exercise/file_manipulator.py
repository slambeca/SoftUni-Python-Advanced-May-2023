import os

COMMAND_END = "End"
COMMAND_CREATE = "Create"
COMMAND_ADD = "Add"
COMMAND_REPLACE = "Replace"
COMMAND_DELETE = "Delete"

while True:
    command = input()    # Create-file.txt

    if command == COMMAND_END:
        break

    command_args = command.split("-")    # ['Replace', 'random.txt', 'Some', 'some']

    current_command = command_args[0]
    file_name = command_args[1]

    if current_command == COMMAND_CREATE:
        file = open(f"{file_name}", "w")

        file.close()

    elif current_command == COMMAND_ADD:
        content = command_args[2]
        file = open(f"{file_name}", "a")
        file.write(f"{content}\n")

        file.close()

    elif current_command == COMMAND_REPLACE:
        old_string = command_args[2]
        new_string = command_args[3]
        
        try:
            file = open(f"{file_name}", "r+")
            text = file.read()
            text = text.replace(old_string, new_string)
            file.seek(0)    # Sets the reference point at the beginning of the file
            file.write(text)

            file.close()

        except FileNotFoundError:
            print("An error occurred")

    elif current_command == COMMAND_DELETE:
        try:
            os.remove(file_name)
        except FileNotFoundError:
            print("An error occurred")