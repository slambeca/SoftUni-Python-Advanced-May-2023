import os

current_directory = input()    # .

dictionary_with_extensions = {}

# print(os.listdir(current_directory))
# ['directory_traversal.py', 'even_lines.py', 'file_manipulator.py', 'line_numbers.py', 'output.txt', 'text.txt']

for file_name in os.listdir(current_directory):    # Can be either folder or a file
    current_file = os.path.join(current_directory, file_name)    # .\directory_traversal.py

    current_file = current_file.lstrip(".\\")

    if os.path.isfile(current_file):
        extension = file_name.split(".")[1]

        if extension not in dictionary_with_extensions.keys():
            dictionary_with_extensions[extension] = []

        dictionary_with_extensions[extension].append(current_file)
    elif os.path.isdir(current_directory):
        pass

sorted_dict = dict(sorted(dictionary_with_extensions.items(), key=lambda x: [x[0]]))

result = []

for keys, values in sorted_dict.items():
    result.append(f".{keys}")
    result.append('\n'.join([f"- - - {value}" for value in values]))

with open("report.txt", "w") as report_file:
    report_file.write('\n'.join(result))
