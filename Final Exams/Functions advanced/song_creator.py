def add_songs(*args):
    dictionary, result = {}, []

    for element in args:
        song_title = element[0]
        text = element[1]

        if song_title not in dictionary.keys():
            dictionary[song_title] = []
        dictionary[song_title].extend(text)

    for title, lyrics in dictionary.items():
        result.append('- ' + title)
        if lyrics:
            result.extend(lyrics)

    return '\n'.join(result)


# print(add_songs(
#     ("Bohemian Rhapsody", []),
#     ("Just in Time",
#      ["Just in time, I found you just in time",
#       "Before you came, my time was running low",
#       "I was lost, the losing dice were tossed",
#       "My bridges all were crossed, nowhere to go"])
# ))

# print(add_songs(
#     ("Beat It", []),
#     ("Beat It",
#      ["Just beat it (beat it), beat it (beat it)",
#       "No one wants to be defeated"]),
#     ("Beat It", []),
#     ("Beat It",
#      ["Showin' how funky and strong is your fight",
#       "It doesn't matter who's wrong or right"]),
# ))
#
# print(add_songs(
#     ("Love of my life",
#      ["Love of my life, you've hurt me",
#       "You've broken my heart, and now you leave me",
#       "Love of my life, can't you see?",
#       "Bring it back, bring it back"]),
#     ("Beat It", []),
#     ("Love of my life",
#      ["Don't take it away from me",
#       "Because you don't know",
#       "What it means to me"]),
#     ("Dream On",
#      ["Every time that I look in the mirror"]),
# ))