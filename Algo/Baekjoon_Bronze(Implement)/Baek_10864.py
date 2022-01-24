import sys

n, m = map(int, sys.stdin.readline().split())

friend = {i+1: 0 for i in range(n)}

for _ in range(m):
    me, other = map(int, sys.stdin.readline().split())

    friend[me] += 1
    friend[other] += 1

for i in friend.values():
    print(i)