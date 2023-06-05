def words_sorting(*args):
    global dictionary

    for word in args:
        if word not in dictionary.keys():
            dictionary[word] = 0
            for letter in word:
                dictionary[word] += ord(letter)

    values_sum = 0

    for key, value in dictionary.items():
        values_sum += int(value)

    if values_sum % 2 == 0:
        result = ""
        dictionary = dict(sorted(dictionary.items(), key=lambda x: x[0]))
        for key, value in dictionary.items():
            result += f"{key} - {value}\n"
        return result
    else:
        result = ""
        dictionary = dict(sorted(dictionary.items(), key=lambda x: -x[1]))
        for key, value in dictionary.items():
            result += f"{key} - {value}\n"
        return result


dictionary = {}

# print(words_sorting(
#     'escape',
#     'charm',
#     'mythology'))

# print(
#     words_sorting(
#         'cacophony',
#         'accolade'
#   ))

# print(
#     words_sorting(
#         'escape',
#         'charm',
#         'eye'
#   ))