import re
from typing import List, Dict


def get_file_content(path_to_file):
    with open(path_to_file, "r") as file:
        text = "".join(file.readlines())
        return re.findall(r"[a-z']+", text.lower())


def write_result(res):
    with open("output.txt", "w") as file:
        # for r in res:
        #     file.write(r+"\n")
        file.writelines("\n".join(res))


path_to_words: List[str] = "words.txt"
path_to_text: List[str] = "text.txt"

first_file_words = get_file_content(path_to_words)
second_file_words = get_file_content(path_to_text)

analyse: Dict[str, int] = {}

for word in first_file_words:
    if word in second_file_words:
        analyse[word] = second_file_words.count(word)

result = [f"{el[0]} - {el[1]}" for el in sorted(analyse.items(), key=lambda x: -x[1])]

write_result(result)