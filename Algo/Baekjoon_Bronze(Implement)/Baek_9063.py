import sys

n = int(sys.stdin.readline())

horizon = []
vertical = []

for _ in range(n):
    x, y = map(int, sys.stdin.readline().split())

    horizon.append(x)
    vertical.append(y)

res_x = max(horizon) - min(horizon)
res_y = max(vertical) - min(vertical)

print(res_x * res_y)