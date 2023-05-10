try:
    with open("test.txt", "r") as file:
        print("File found")
except FileNotFoundError:
    print("File not found")