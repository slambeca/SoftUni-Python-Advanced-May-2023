from collections import deque

eggs = deque(map(int, input().split(", ")))
papers = deque(map(int, input().split(", ")))

boxes = 0

BOX_SIZE = 50
BAD_LUCK = 13

while eggs and papers:
    first_egg = eggs.popleft()    # 20

    if first_egg <= 0:
        continue

    if first_egg == BAD_LUCK:
        first_piece_of_paper = papers.popleft()
        last_piece_of_paper = papers.pop()
        papers.appendleft(last_piece_of_paper)
        papers.append(first_piece_of_paper)
        continue

    last_piece_paper = papers.pop()    # 9

    total_sum = first_egg + last_piece_paper    # 29

    if total_sum <= BOX_SIZE:
        boxes += 1
    else:
        continue

if boxes:
    print(f"Great! You filled {boxes} boxes.")
else:
    print(f"Sorry! You couldn't fill any boxes!")

if eggs:
    print(f"Eggs left: {', '.join(str(x) for x in eggs)}")
if papers:
    print(f"Pieces of paper left: {', '.join(str(x) for x in papers)}")