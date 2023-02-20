import sys

n, m = map(int, sys.stdin.readline().split())

bucket = [0 for i in range(n+1)]

for i in range(m):
    i, j, k = map(int, sys.stdin.readline().split())

    for ball in range(i, j+1):
        bucket[ball] = k

for result in range(1, len(bucket)):
    print(bucket[result], end=" ")