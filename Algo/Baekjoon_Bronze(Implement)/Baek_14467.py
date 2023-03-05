import sys

n = int(sys.stdin.readline())

status = dict()
move = 0

for _ in range(n):
    cow, loc = map(int, sys.stdin.readline().split())

    if cow in status and status[cow] != loc:
        move += 1

    status[cow] = loc

print(move)