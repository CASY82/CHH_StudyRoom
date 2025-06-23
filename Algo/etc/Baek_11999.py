import sys

x, y, m = map(int, sys.stdin.readline().split())

can_x = m // x
can_y = m // y
res = 0

for i in range(can_x + 1):
    for j in range(can_y + 1):
        if x * i + y * j <= m:
            res = max(x * i + y * j, res)

print(res)