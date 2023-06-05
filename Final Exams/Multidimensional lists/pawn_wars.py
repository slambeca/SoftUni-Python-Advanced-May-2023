# Not finished -> 90/100 in Judge TODO
ROWS, COLUMNS = 8, 8

chess_board = []
# - - - - - - b -
# - - - - - - - -
# - - - - - - - -
# - - - - - - - -
# - - - - - - - -
# - w - - - - - -
# - - - - - - - -
# - - - - - - - -

white_pawn_pos = []  # [5, 1]
black_pawn_pos = []  # [0, 6]

for row in range(ROWS):
    chess_board.append(input().split())

    if "w" in chess_board[row]:
        white_pawn_pos = [row, chess_board[row].index("w")]
    if "b" in chess_board[row]:
        black_pawn_pos = [row, chess_board[row].index("b")]

directions = {
    "up": (-1, 0),
    "down": (1, 0),
}

rows, cols = {
                 0: 8,
                 1: 7,
                 2: 6,
                 3: 5,
                 4: 4,
                 5: 3,
                 6: 2,
                 7: 1,
             }, {
                 0: "a",
                 1: "b",
                 2: "c",
                 3: "d",
                 4: "e",
                 5: "f",
                 6: "g",
                 7: "h",
             }

index = 1

while True:
    if index % 2 != 0:
        first_diagonal_row = white_pawn_pos[0] - 1
        first_diagonal_col = white_pawn_pos[1] - 1
        second_diagonal_row = white_pawn_pos[0] - 1
        second_diagonal_col = white_pawn_pos[1] + 1

        if (0 <= first_diagonal_row < ROWS and 0 <= first_diagonal_col < COLUMNS) or \
                (0 <= second_diagonal_row < ROWS and 0 <= second_diagonal_col < COLUMNS):
            if chess_board[first_diagonal_row][first_diagonal_col] == "b" or \
                    chess_board[second_diagonal_row][second_diagonal_col] == "b":
                print(f"Game over! White win, capture on {cols[black_pawn_pos[1]]}{rows[black_pawn_pos[0]]}.")
                break

        wanted_row = white_pawn_pos[0] + directions["up"][0]
        wanted_col = white_pawn_pos[1] + directions["up"][1]

        chess_board[white_pawn_pos[0]][white_pawn_pos[1]] = "-"
        chess_board[wanted_row][wanted_col] = "w"
        white_pawn_pos = [wanted_row, wanted_col]

        if wanted_row == 0:
            print(f"Game over! White pawn is promoted to a queen at {cols[wanted_col]}{rows[wanted_row]}.")
            break

    else:
        first_diagonal_row = black_pawn_pos[0] + 1
        first_diagonal_col = black_pawn_pos[1] - 1
        second_diagonal_row = black_pawn_pos[0] + 1
        second_diagonal_col = black_pawn_pos[1] + 1

        if (0 <= first_diagonal_row < ROWS and 0 <= first_diagonal_col < COLUMNS) or \
                (0 <= second_diagonal_row < ROWS and 0 <= second_diagonal_col < COLUMNS):
            if chess_board[first_diagonal_row][first_diagonal_col] == "w" or \
                    chess_board[second_diagonal_row][second_diagonal_col] == "w":
                print(f"Game over! Black win, capture on {cols[white_pawn_pos[1]]}{rows[white_pawn_pos[0]]}.")
                break

        wanted_row = black_pawn_pos[0] + directions["down"][0]
        wanted_col = black_pawn_pos[1] + directions["down"][1]

        chess_board[black_pawn_pos[0]][black_pawn_pos[1]] = "-"
        chess_board[wanted_row][wanted_col] = "b"
        black_pawn_pos = [wanted_row, wanted_col]

        if wanted_row == ROWS - 1:
            print(f"Game over! Black pawn is promoted to a queen at {cols[wanted_col]}{rows[wanted_row]}.")
            break

    index += 1
