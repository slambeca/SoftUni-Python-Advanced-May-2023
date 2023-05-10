numbers = [int(x) for x in input().split()]    # [1, 2, 3, 4, 5]

reversed_numbers = []

while len(numbers):
    current_number = numbers.pop()

    reversed_numbers.append(current_number)

print(*reversed_numbers, sep=" ")

# Variant 2
from collections import deque

text = deque(input().split())

text.reverse()

print(" ".join(text))

# Variant 3
print(*input().split()[::-1], sep=" ")

# Variant 4
from collections import deque

numbers = deque(input().split())

for _ in range(len(numbers)):
    print(numbers.pop(), end=" ")
