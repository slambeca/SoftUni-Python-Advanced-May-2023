def accommodate_new_pets(capacity, max_weight, *pets):
    accommodated_pets = {}
    result = []

    for pet_type, pet_weight in pets:
        if capacity == 0:
            result.append('You did not manage to accommodate all pets!')
            break

        if pet_weight > max_weight:
            continue

        if pet_type not in accommodated_pets:
            accommodated_pets[pet_type] = 0
        accommodated_pets[pet_type] += 1

        capacity -= 1

    else:
        result.append(f'All pets are accommodated! Available capacity: {capacity}.')

    result.append('Accommodated pets:')
    [result.append(f'{pet_type}: {pet_number}') for pet_type, pet_number in sorted(accommodated_pets.items())]
    return '\n'.join(result)


print(accommodate_new_pets(
    10,
    10.0,
    ("cat", 5.8),
    ("dog", 10.5),
    ("parrot", 0.8),
    ("cat", 3.1),
))
