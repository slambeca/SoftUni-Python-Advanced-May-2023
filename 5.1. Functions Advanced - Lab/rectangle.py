def rectangle(length, width):
    def area():
        return length * width

    def perimeter():
        return (length * 2) + (width * 2)

    if type(length) != int or type(width) != int:
        return "Enter valid values!"

    return f"""Rectangle area: {area()}
Rectangle perimeter: {perimeter()}"""


print(rectangle(2, 10))
print(rectangle('2', 10))