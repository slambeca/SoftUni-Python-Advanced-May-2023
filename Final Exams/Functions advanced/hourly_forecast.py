def forecast(*args):
    dictionary = {}
    sunny, cloudy, rainy, result = "", "", "", ""

    for item in args:
        city, weather = item[0], item[1]

        if city not in dictionary.keys():
            dictionary[city] = weather

    sorted_dictionary = dict(sorted(dictionary.items(), key=lambda x: x[0]))

    for key, value in sorted_dictionary.items():
        if value == "Sunny":
            sunny += f"{key} - {value}\n"
        elif value == "Cloudy":
            cloudy += f"{key} - {value}\n"
        else:
            rainy += f"{key} - {value}\n"

    result = sunny + cloudy + rainy

    return result


# print(forecast(
#     ("Sofia", "Sunny"),
#     ("London", "Cloudy"),
#     ("New York", "Sunny")))
#
# print(forecast(
#     ("Beijing", "Sunny"),
#     ("Hong Kong", "Rainy"),
#     ("Tokyo", "Sunny"),
#     ("Sofia", "Cloudy"),
#     ("Peru", "Sunny"),
#     ("Florence", "Cloudy"),
#     ("Bourgas", "Sunny")))

# print(forecast(
#     ("Tokyo", "Rainy"),
#     ("Sofia", "Rainy")))
