import sys

n = int(sys.stdin.readline())
schedule = list(map(int, sys.stdin.readline().split()))
real = list(map(int, sys.stdin.readline().split()))
res = 0

for i in range(n):
    if schedule[i] <= real[i]:
        res += 1

print(res)