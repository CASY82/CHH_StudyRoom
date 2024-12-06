import sys

n, m = map(int, sys.stdin.readline().split())
satisfied = list(map(int, sys.stdin.readline().split()))
pay = list(map(int, sys.stdin.readline().split()))

satisfied.sort(reverse=True)
pay.sort()

res = 0

for i in range(min(n, m)):
    res += max(satisfied[i] - pay[i], 0)

print(res)