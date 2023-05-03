line = input().split("|")

matrix = []

for substring in line[::-1]:
    matrix.extend(substring.split())    # We remove all the spaces

print(*matrix)