import sys

t = int(sys.stdin.readline())

for _ in range(t):
    d = int(sys.stdin.readline())
    time = 0

    while time + time * time <= d:
        time += 1

    print(time-1)