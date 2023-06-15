def fix_calendar(calendar):
    n = len(calendar)

    for i in range(n):
        swapped = False

        for j in range(0, n - i - 1):
            if calendar[j] > calendar[j + 1]:
                calendar[j], calendar[j + 1] = calendar[j + 1], calendar[j]
                swapped = True

        if not swapped:
            break

    return calendar


numbers = [3, 2, 1]
fixed = fix_calendar(numbers)
print(fixed)