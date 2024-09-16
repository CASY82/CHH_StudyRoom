import sys

n, k = map(int, sys.stdin.readline().split())
routine = []
res = 0

for _ in range(n):
    score = int(sys.stdin.readline())

    routine.append(score)

routine.sort(reverse=True)

for i in range(k):
    res += routine[i]

print(res)