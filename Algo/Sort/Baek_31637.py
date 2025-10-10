import sys

n, d = map(int, sys.stdin.readline().split())
child_height = list(map(int, sys.stdin.readline().split()))
res = True

child_height.sort()

for i in range(0, n * 2, 2):
    if child_height[i + 1] - child_height[i] > d:
        res = False

if res:
    print("Yes")
else:
    print("No")