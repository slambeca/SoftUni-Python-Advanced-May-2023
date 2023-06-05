# This custom module is for exercise 5.fibonacci_sequence
seq = [0, 1]


def create_sequence(n):
    global seq
    if n == 0:
        return []
    elif n == 1:
        return [0]

    seq = [0, 1]
    for _ in range(2, n):
        seq.append(seq[-1] + seq[-2])

    return ' '.join(str(x) for x in seq)


def locate(x):
    if x in seq:
        return f"The number - {x} is at index {seq.index(x)}"
    else:
        return f"The number {x} is not in the sequence"