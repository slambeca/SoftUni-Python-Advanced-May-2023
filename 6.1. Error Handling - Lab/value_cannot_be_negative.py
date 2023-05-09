class ValueCannotBeNegativeError(Exception):    # Good practice is for the exceptions name to end with Error
    """This is our custom exception, the name makes it self-explicit"""
    pass


while True:
    num = int(input())

    if num < 0:
        raise ValueCannotBeNegativeError(f"{num} is negative!")