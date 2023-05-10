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