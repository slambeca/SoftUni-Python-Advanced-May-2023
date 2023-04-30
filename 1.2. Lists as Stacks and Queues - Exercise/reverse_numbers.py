# Using a stack
numbers = [int(x) for x in input().split()]    # [1, 2, 3, 4, 5]

reversed_numbers = []

while len(numbers):
    current_number = numbers.pop()

    reversed_numbers.append(current_number)

print(*reversed_numbers, sep=" ")

# 100/100 in Judge

# Using a deque
from collections import deque

text = deque(input().split())

text.reverse()

print(" ".join(text))

# 100/100 in Judge

# One-liner
print(*input().split()[::-1], sep=" ")

# 100/100 in Judge