from collections import deque

vowels = deque(x for x in input().split())    # deque(['o', 'e', 'a', 'o', 'e', 'a', 'i'])
consonants = [x for x in input().split()]    # ['p', 'r', 's', 'x', 'r']

rose, tulip, lotus, daffodil = [], [], [], []

flower_found = False

while not flower_found and vowels and consonants:
    current_vowel = vowels.popleft()    # o
    current_consonant = consonants.pop()    # r

    if current_vowel in "rose" and current_vowel not in rose:
        rose.append(current_vowel)
        if len(rose) == len("rose"):
            print("Word found: rose")
            flower_found = True
            break
    if current_consonant in "rose" and current_consonant not in rose:
        rose.append(current_consonant)
        if len(rose) == len("rose"):
            print("Word found: rose")
            flower_found = True
            break

    if current_vowel in "tulip" and current_vowel not in tulip:
        tulip.append(current_vowel)
        if len(tulip) == len("tulip"):
            print("Word found: tulip")
            flower_found = True
            break
    if current_consonant in "tulip" and current_consonant not in tulip:
        tulip.append(current_consonant)
        if len(tulip) == len("tulip"):
            print("Word found: tulip")
            flower_found = True
            break

    if current_vowel in "lotus" and current_vowel not in lotus:
        lotus.append(current_vowel)
        if len(lotus) == len("lotus"):
            print("Word found: lotus")
            flower_found = True
            break
    if current_consonant in "lotus" and current_consonant not in lotus:
        lotus.append(current_consonant)
        if len(lotus) == len("lotus"):
            print("Word found: lotus")
            flower_found = True
            break

    if current_vowel in "daffodil" and current_vowel not in daffodil:
        daffodil.append(current_vowel)
        if len(daffodil) == 5:
            print("Word found: daffodil")
            flower_found = True
            break
    if current_consonant in "daffodil" and current_consonant not in daffodil:
        daffodil.append(current_consonant)
        if len(daffodil) == 5:
            print("Word found: daffodil")
            flower_found = True
            break

if not flower_found:
    print("Cannot find any word!")
if vowels:
    print(f"Vowels left: {' '.join(x for x in vowels)}")
if consonants:
    print(f"Consonants left: {' '.join(x for x in consonants)}")

# Variant 2
# from collections import deque
#
# vowels = deque(x for x in input().split())    # deque(['o', 'e', 'a', 'o', 'e', 'a', 'i'])
# consonants = [x for x in input().split()]    # ['p', 'r', 's', 'x', 'r']
#
# flower_1, flower_2, flower_3, flower_4 = "rose", "tulip", "lotus", "daffodil"
#
# while vowels and consonants:
#     current_vowel = vowels.popleft()
#     current_consonant = consonants.pop()
#     if current_vowel in flower_1:
#         flower_1 = flower_1.replace(current_vowel, "")
#     if current_vowel in flower_2:
#         flower_2 = flower_2.replace(current_vowel, "")
#     if current_vowel in flower_3:
#         flower_3 = flower_3.replace(current_vowel, "")
#     if current_vowel in flower_4:
#         flower_4 = flower_4.replace(current_vowel, "")
#
#     if current_consonant in flower_1:
#         flower_1 = flower_1.replace(current_consonant, "")
#     if current_consonant in flower_2:
#         flower_2 = flower_2.replace(current_consonant, "")
#     if current_consonant in flower_3:
#         flower_3 = flower_3.replace(current_consonant, "")
#     if current_consonant in flower_4:
#         flower_4 = flower_4.replace(current_consonant, "")
#
#     if not flower_1 or not flower_2 or not flower_3 or not flower_4:
#         break
#
# if not flower_1:
#     print("Word found: rose")
# elif not flower_2:
#     print("Word found: tulip")
# elif not flower_3:
#     print("Word found: lotus")
# elif not flower_4:
#     print("Word found: daffodil")
# else:
#     print("Cannot find any word!")
# if vowels:
#     print(f"Vowels left: {' '.join(x for x in vowels)}")
# if consonants:
#     print(f"Consonants left: {' '.join(x for x in consonants)}")

# Variant 3 with pseudocode
# 1. Read the two sequences and save them in deque
# 2. Define dictionary with key = word and value = word
# 3. While we have sequences of letters, we pop from the sequences
# 4. Iterate through every word in the searched words
#   - remove all occurrences of the vowel and consonant in the value of the word dict
#   - check if we have empty string as a value
#        - print that a word was found and break loops
# 5. Print the rest of the needed output
# 
# from collections import deque
# 
# vowels = deque(input().split())
# consonants = deque(input().split())
# 
# words = {
#     "rose": "rose",
#     "tulip": "tulip",
#     "lotus": "lotus",
#     "daffodil": "daffodil",
# }
# 
# while vowels and consonants:
#     vowel = vowels.popleft()
#     consonant = consonants.pop()
# 
#     for word in words.keys():
#         words[word] = words[word].replace(vowel, "")
#         words[word] = words[word].replace(consonant, "")
# 
#         if not words[word]:
#             print(f"Word found: {word}")
#             break
# 
#     else:
#         continue
# 
#     break
# 
# else:
#     print("Cannot find any word!")
# 
# if vowels:
#     print(f"Vowels left: {' '.join(vowels)}")
# if consonants:
#     print(f"Consonants left: {' '.join(consonants)}")
