import sys

while True:
    now, action, after = sys.stdin.readline().strip().split()

    if now == "0" and action == "W" and after == "0":
        break

    now = int(now)
    after = int(after)

    if action == "W":
        now -= after
    else:
        now += after

    if now < -200:
        print("Not allowed")
    else:
        print(now)