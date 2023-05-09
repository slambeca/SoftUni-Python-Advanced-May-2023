def check_values(some_text, times_to_repeat_it):
    return some_text * int(times_to_repeat_it)


text = input()
times = input()

try:
    print(check_values(text, times))
except ValueError:
    print("Variable times must be an integer")
# finally:
#     print("Exception handled successfully!")