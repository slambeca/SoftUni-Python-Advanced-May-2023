players = input().split(", ")
player_one, player_two = players[0], players[1]

index = 1
SIZE = 6

matrix = []
# . . T . . .
# . . . . . .
# . . W . . .
# . . W . . E
# . . . . . .
# . T . W . .

player_one_resting, player_two_resting = False, False

for row in range(SIZE):
    matrix.append(input().split())

while True:
    coordinates = input().split(", ")
    wanted_row, wanted_col = int(coordinates[0].strip("(")), int(coordinates[1].strip(")"))

    if index % 2 != 0:
        if player_one_resting:
            player_one_resting = False
            index += 1
            continue

        if matrix[wanted_row][wanted_col] == "E":
            print(f"{player_one} found the Exit and wins the game!")
            break
        elif matrix[wanted_row][wanted_col] == "T":
            print(f"{player_one} is out of the game! The winner is {player_two}.")
            break
        elif matrix[wanted_row][wanted_col] == "W":
            print(f"{player_one} hits a wall and needs to rest.")
            player_one_resting = True

    else:
        if player_two_resting:
            player_two_resting = False
            index += 1
            continue

        if matrix[wanted_row][wanted_col] == "E":
            print(f"{player_two} found the Exit and wins the game!")
            break
        elif matrix[wanted_row][wanted_col] == "T":
            print(f"{player_two} is out of the game! The winner is {player_one}.")
            break
        elif matrix[wanted_row][wanted_col] == "W":
            print(f"{player_two} hits a wall and needs to rest.")
            player_two_resting = True

    index += 1