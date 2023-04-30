from collections import deque

player_names = input().split()    # ['Tracy', 'Emilly', 'Daniels']

step_of_hot_potato = int(input())    # 2

players_deque = deque(player_names)    # deque(['Tracy', 'Emilly', 'Daniels'])
current_position = 0

while len(players_deque) > 1:
    current_position += 1
    current_name_of_player = players_deque.popleft()

    if current_position == step_of_hot_potato:
        print(f"Removed {current_name_of_player}")
        current_position = 0
    else:
        players_deque.append(current_name_of_player)

print(f"Last is {players_deque[0]}")

# # Variant 2
# from collections import deque
#
# player_names = input().split()    # ['Tracy', 'Emilly', 'Daniels']
#
# step_of_hot_potato = int(input())    # 2
#
# players_deque = deque(player_names)    # deque(['Tracy', 'Emilly', 'Daniels'])
#
# while len(players_deque) > 1:
#     for _ in range(step_of_hot_potato - 1):
#         players_deque.append(players_deque.popleft())
#
#     print(f"Removed {players_deque.popleft()}")
#
# print(f"Last is {players_deque[0]}")