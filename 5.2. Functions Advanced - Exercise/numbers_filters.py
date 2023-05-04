def even_odd_filter(**numbers):
    if "odd" in numbers:
        numbers["odd"] = [x for x in numbers["odd"] if int(x) % 2 != 0]

    if "even" in numbers:
        numbers["even"] = list(filter(lambda x: x % 2 == 0, numbers["even"]))

    return dict(sorted(numbers.items(), key=lambda x: -len(x[1])))


print(even_odd_filter(
    odd=[1, 2, 3, 4, 10, 5],
    even=[3, 4, 5, 7, 10, 2, 5, 5, 2],
))

print(even_odd_filter(
    odd=[2, 2, 30, 44, 10, 5],
))