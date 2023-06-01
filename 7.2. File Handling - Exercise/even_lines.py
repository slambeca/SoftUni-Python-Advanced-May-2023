symbols = ["-", ",", ".", "!", "?"]

with open("text.txt", "r") as file:
    text = file.readlines()
    # ["-I was quick to judge him, but it wasn't his fault.\n", '-Is this some kind of joke?! Is it?\n',
    # '-Quick, hide here. It is safer.']

for row in range(0, len(text), 2):
    for symbol in symbols:
        text[row] = text[row].replace(symbol, "@")

    print(*text[row].split()[::-1])