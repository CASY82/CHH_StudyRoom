import sys

t = int(sys.stdin.readline())

for _ in range(t):
    n, m = map(int, sys.stdin.readline().split())

    hubo = [0] * n

    for i in range(m):
        votes = list(map(int, sys.stdin.readline().split()))
        for j in range(n):
            hubo[j] += votes[j]

    print(hubo.index(max(hubo)) + 1)