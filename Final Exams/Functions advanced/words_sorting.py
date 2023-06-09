def words_sorting(*args):
    dictionary, result = {}, ""

    for word in args:
        if word not in dictionary.keys():
            dictionary[word] = 0
            for letter in word:
                dictionary[word] += ord(letter)

    values_sum = 0

    for key, value in dictionary.items():
        values_sum += int(value)

    if values_sum % 2 == 0:
        dictionary = dict(sorted(dictionary.items(), key=lambda x: x[0]))

        for key, value in dictionary.items():
            result += f"{key} - {value}\n"

    else:
        dictionary = dict(sorted(dictionary.items(), key=lambda x: -x[1]))

        for key, value in dictionary.items():
            result += f"{key} - {value}\n"

    return result

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

# Variant 2


# def words_sorting(*words):
#     words_dict = {word: sum(map(ord, word)) for word in words}
#
#     total_sum = sum(words_dict.values())
#
#     if total_sum % 2 == 0:
#         return '\n'.join([f"{w} - {s}" for w, s in sorted(words_dict.items(), key=lambda x: x[0])])
#
#     return '\n'.join([f"{w} - {s}" for w, s in sorted(words_dict.items(), key=lambda x: -x[1])])
