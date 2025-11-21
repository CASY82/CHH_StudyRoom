import sys

n = int(sys.stdin.readline())

squad = []
tmp = []

for _ in range(n):
    s = int(sys.stdin.readline())

    squad.append(s)

squad.sort()

for i in range(n // 2):
    tmp.append(squad[i] + squad[n - 1 - i])

print(min(tmp))