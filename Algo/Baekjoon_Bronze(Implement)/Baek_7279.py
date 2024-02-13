import sys

n, k = map(int, sys.stdin.readline().split())
now = 0
max_standup = 0

for _ in range(n):
    in_bus, out_bus = map(int, sys.stdin.readline().split())

    now += in_bus
    now -= out_bus

    if now > k:
        max_standup = max(max_standup, now - k)

print(max_standup)