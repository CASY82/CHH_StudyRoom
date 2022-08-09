import sys

n, m = map(int, sys.stdin.readline().split())

friends = [[] for _ in range(n)]

for _ in range(m):
    fir, sec = map(int, sys.stdin.readline().split())

    friends[fir-1].append(sec)
    friends[sec-1].append(fir)

for i in range(n):
    print(len(friends[i]))