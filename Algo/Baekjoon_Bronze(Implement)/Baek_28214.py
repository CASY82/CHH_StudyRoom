import sys

n, k, p = map(int, sys.stdin.readline().split())
bread = list(map(int, sys.stdin.readline().split()))

result = 0

for i in range(n):
    no_cream = 0
    for j in range(k):
        if bread[i * k + j] == 0:
            no_cream += 1

    if no_cream < p:
        result += 1

print(result)