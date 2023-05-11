from collections import deque

bullet_price = int(input())
gun_barrel = int(input())

bullets = [int(x) for x in input().split()]
locks = deque(int(x) for x in input().split())

intelligence = int(input())

total_sum_spend = 0
barrel_count = 0
bullets_count = 0

while bullets and locks:
    total_sum_spend += bullet_price
    current_bullet = bullets.pop()
    current_lock = locks[0]
    barrel_count += 1
    bullets_count += 1

    if current_bullet <= current_lock:
        print("Bang!")
        locks.popleft()

    elif current_bullet > current_lock:
        print("Ping!")

    if barrel_count == gun_barrel and bullets:
        print("Reloading!")
        barrel_count = 0

if not locks:
    print(f"{len(bullets)} bullets left. Earned ${intelligence - total_sum_spend}")
else:
    print(f"Couldn't get through. Locks left: {len(locks)}")

# Variant 2
# from collections import deque
#
# bullet_price = int(input())    # 50
# gun_barrel_size = int(input())    # 2
# bullets = [int(x) for x in input().split()]    # [11, 10, 5, 11, 10, 20]
# locks = deque([int(x) for x in input().split()])    # deque([15, 13, 16])
# intelligence_value = int(input())    # 1500
#
# bullets_left = gun_barrel_size    # 2
#
# while bullets and locks:
#     current_bullet = bullets.pop()    # 20
#     current_lock = locks.popleft()    # 15
#
#     if current_lock >= current_bullet:
#         print("Bang!")
#         bullets_left -= 1
#         intelligence_value -= bullet_price
#     else:
#         print("Ping!")
#         locks.appendleft(current_lock)
#         bullets_left -= 1
#         intelligence_value -= bullet_price
#
#     if bullets_left == 0:
#         if bullets:
#             print("Reloading!")
#             bullets_left = gun_barrel_size
#
# if not locks:
#     print(f"{len(bullets)} bullets left. Earned ${intelligence_value}")
# else:
#     print(f"Couldn't get through. Locks left: {len(locks)}")
