def movie_organizer(*args):
    dictionary = {}
    result = []

    for item in args:
        movie, genre = item[0], item[1]

        if genre not in dictionary.keys():
            dictionary[genre] = []
        dictionary[genre].append(movie)

    for keys, values in dictionary.items():
        values.sort()

    sorted_dictionary = dict(sorted(dictionary.items(), key=lambda x: (-len(x[1]), x[0])))

    for key, values in sorted_dictionary.items():
        result.append(f"{key} - {len(values)}")
        for value in values:
            result.append(f"* {value}")

    return '\n'.join(result)


print(movie_organizer(
    ("The Matrix", "Sci-fi")))

# print(movie_organizer(
#     ("The Godfather", "Drama"),
#     ("The Hangover", "Comedy"),
#     ("The Shawshank Redemption", "Drama"),
#     ("The Pursuit of Happiness", "Drama"),
#     ("The Hangover Part II", "Comedy")))

# print(movie_organizer(
#     ("Avatar: The Way of Water", "Action"),
#     ("House Of Gucci", "Drama"),
#     ("Top Gun", "Action"),
#     ("Ted", "Comedy"),
#     ("Duck Soup", "Comedy"),
#     ("The Dark Knight", "Action"),
#     ("A Star Is Born", "Musicals"),
#     ("The Warrior", "Action"),
#     ("Like A Boss", "Comedy"),
#     ("The Green Mile", "Drama"),
#     ("21 Jump Street", "Comedy")))