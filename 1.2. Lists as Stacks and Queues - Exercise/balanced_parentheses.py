# Corner case is {{{}}}} - one more closing bracket than opening
parentheses = input()    # {[()]}

openings = ("{", "[", "(")

pair_one = ("{", "}")
pair_two = ("(", ")")
pair_three = ("[", "]")

stack = []
closings = []

for symbol in parentheses:
    if symbol in openings:
        stack.append(symbol)
    else:
        closings.append(symbol)
        if stack:
            if (stack[-1] in pair_one and symbol in pair_one) or (stack[-1] in pair_two and symbol in pair_two)\
                    or (stack[-1] in pair_three and symbol in pair_three):
                stack.pop()
                closings.pop()

if not stack and not closings:
    print("YES")
else:
    print("NO")

# Variant 2
# from collections import deque

# parentheses = deque(input())  # deque(['{', '[', '(', ')', ']', '}'])

# opened_parentheses = deque()

# while parentheses:
#     left_parenthesis = parentheses.popleft()

#     if left_parenthesis in "{([":
#         opened_parentheses.append(left_parenthesis)
#     elif not opened_parentheses:
#         print("NO")
#         break
#     else:
#         if f"{opened_parentheses.pop() + left_parenthesis}" not in "{}()[]":
#             print("NO")
#             break
# else:
#     print("YES")
