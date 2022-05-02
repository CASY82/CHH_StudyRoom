import sys

x1, y1, r1 = map(int, sys.stdin.readline().split())
x2, y2, r2 = map(int, sys.stdin.readline().split())

result = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5

if (r1 + r2) > result:
    print("YES")
else:
    print("NO")