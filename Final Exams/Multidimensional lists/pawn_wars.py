SIZE = 8
board = []
positions = [[], []]


def save_positions(search_for, index_to_save, r):
    if search_for in board[r]:
        positions[index_to_save].append(r)
        positions[index_to_save].append(board[r].index(search_for))


for row in range(SIZE):
    board.append(input().split())

    save_positions("w", 0, row)
    save_positions("b", 1, row)

if abs(positions[0][1] - positions[1][1]) != 1:    # The pawns do not encounter each other
    if SIZE - positions[0][0] - 1 <= positions[1][0]:
        print(f"Game over! Black pawn is promoted to a queen at {chr(97 + positions[1][1])}1.")
    else:
        print(f"Game over! White pawn is promoted to a queen at {chr(97 + positions[0][1])}8.")
else:    # The pawns encounter each other
    place = (positions[0][0] + positions[1][0]) // 2
    if positions[0][0] % 2 == positions[1][0] % 2:
        print(f"Game over! Black win, capture on {chr(97 + positions[0][1])}{SIZE - place}.")
    else:
        print(f"Game over! White win, capture on {chr(97 + positions[1][1])}{SIZE - place}.")

# Variant 2
# white_position, black_position, chess_board = [], [], []

# rows = {0: 8, 1: 7, 2: 6, 3: 5, 4: 4, 5: 3, 6: 2, 7: 1}
# cols = {0: "a", 1: "b", 2: "c", 3: "d", 4: "e", 5: "f", 6: "g", 7: "h"}
#
# for row in range(8):
#     chess_board.append(input().split())

#     if "w" in chess_board[row]:
#         white_position = [row, chess_board[row].index("w")]
#     if "b" in chess_board[row]:
#         black_position = [row, chess_board[row].index("b")]
#
# if abs(white_position[1] - black_position[1]) != 1:    # The pawns do not encounter each other
#     if 8 - black_position[0] > white_position[0]:
#         print(f"Game over! White pawn is promoted to a queen at {cols[white_position[1]]}8.")
#     else:
#         print(f"Game over! Black pawn is promoted to a queen at {cols[black_position[1]]}1.")
# else:    # The pawns encounter each other
#     position_of_encounter = (white_position[0] + black_position[0]) // 2
#     if abs(white_position[0] - black_position[0]) % 2 != 0:
#         print(f"Game over! White win, capture on {cols[black_position[1]]}{rows[position_of_encounter]}.")
#     else:
#         print(f"Game over! Black win, capture on {cols[white_position[1]]}{rows[position_of_encounter]}.")
