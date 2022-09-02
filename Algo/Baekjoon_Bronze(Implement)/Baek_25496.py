import sys

p, n = map(int, sys.stdin.readline().split())
needy = list(map(int, sys.stdin.readline().split()))
cnt = 0

needy.sort()

for i in range(n):
    if p < 200:
        cnt += 1
        p += needy[i]
    else:
        break

print(cnt)