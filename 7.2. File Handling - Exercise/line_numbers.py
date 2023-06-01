from string import punctuation    # All the punctuation symbols in one place

with open("text.txt", "r") as file:
    text = file.readlines()
    # ["-I was quick to judge him, but it wasn't his fault.\n", '-Is this some kind of joke?! Is it?\n',
    # '-Quick, hide here. It is safer.']

output_file = open("output.txt", "w")

for row in range(len(text)):
    letters = 0
    punctuation_symbols = 0

    for symbol in text[row]:
        if symbol.isalpha():
            letters += 1
        elif symbol in punctuation:
            punctuation_symbols += 1

    output_file.write(f"Line {row + 1}: {''.join(text[row][:-1])} ({letters})({punctuation_symbols})\n")

output_file.close()