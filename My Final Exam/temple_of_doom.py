from collections import deque

tools = deque(int(x) for x in input().split())
substances = [int(x) for x in input().split()]
challenges = [int(x) for x in input().split()]

while challenges:
    current_tool = tools.popleft()
    current_substance = substances.pop()

    current_result = current_tool * current_substance

    if current_result in challenges:
        challenges.remove(current_result)
    else:
        tools.append(current_tool + 1)
        substances.append(current_substance - 1)

        if substances[-1] == 0:
            substances.pop()

    if len(substances) == 0:
        break

if not challenges:
    print("Harry found an ostracon, which is dated to the 6th century BCE.")
else:
    print("Harry is lost in the temple. Oblivion awaits him.")

if tools:
    print(f"Tools: {', '.join(str(x) for x in tools)}")
if substances:
    print(f"Substances: {', '.join(str(x) for x in substances)}")
if challenges:
    print(f"Challenges: {', '.join(str(x) for x in challenges)}")