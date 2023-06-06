def flights(*args):
    dictionary = {}

    for word in range(0, len(args) - 1, 2):
        city = args[word]

        if city == "Finish":
            break

        count_people = int(args[word + 1])

        if city not in dictionary.keys():
            dictionary[city] = 0
        dictionary[city] += count_people

    return dictionary


# print(flights('Vienna', 256, 'Vienna', 26, 'Morocco', 98, 'Paris', 115, 'Finish', 'Paris', 15))
# print(flights('London', 0, 'New York', 9, 'Aberdeen', 215, 'Sydney', 2, 'New York', 300, 'Nice', 0, 'Finish'))
# print(flights('Finish', 'New York', 90, 'Aberdeen', 300, 'Sydney', 0))