import sys

b, n, m = map(int, sys.stdin.readline().split())

items = dict()

for _ in range(n):
    item, cost = sys.stdin.readline().strip().split()

    items[item] = int(cost)

tmp_res = 0

for _ in range(m):
    buy = sys.stdin.readline().strip()

    tmp_res += items[buy]

if tmp_res <= b:
    print("acceptable")
else:
    print("unacceptable")