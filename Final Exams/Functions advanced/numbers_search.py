def numbers_searching(*numbers):
    duplicates = []
    missing_value = None
    smallest_number = min(numbers)
    largest_number = max(numbers)

    unique_numbers = set()

    for num in numbers:
        if num in unique_numbers:
            duplicates.append(num)
        unique_numbers.add(num)

    for num in range(smallest_number, largest_number + 1):
        if num not in unique_numbers:
            missing_value = num

    return [missing_value, sorted(list(set(duplicates)))]


print(numbers_searching(1, 2, 4, 2, 5, 4))
print(numbers_searching(5, 5, 9, 10, 7, 8, 7, 9))
print(numbers_searching(50, 50, 47, 47, 48, 45, 49, 44, 47, 45, 44, 44, 48, 44, 48))