import sys

n, k = map(int, sys.stdin.readline().split())
now = 0
save = 0

for _ in range(n):
    command = sys.stdin.readline().strip()

    if command == "ammo":
        now += k
    elif command == "shoot":
        now -= 1
    elif command == "save":
        save = now
    elif command == "load":
        now = save

    print(now)
