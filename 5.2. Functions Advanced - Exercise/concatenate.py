def concatenate(*args, **kwargs):
    text = "".join(args)

    for key in kwargs:
        text = text.replace(key, kwargs[key])

    return text


print(concatenate("Soft", "UNI", "Is", "Grate", "!", UNI="Uni", Grate="Great"))
print(concatenate("I", " ", "Love", " ", "Cythons", C="P", s="", java='Java'))

# Variant 2
#
#
# def concatenate(*args, **kwargs):
#     final_string = "".join(args)
# 
#     for key, value in kwargs.items():
#         final_string = final_string.replace(key, value)
# 
#     return final_string
# 
# 
# print(concatenate("Soft", "UNI", "Is", "Grate", "!", UNI="Uni", Grate="Great"))
# print(concatenate("I", " ", "Love", " ", "Cythons", C="P", s="", java='Java'))
