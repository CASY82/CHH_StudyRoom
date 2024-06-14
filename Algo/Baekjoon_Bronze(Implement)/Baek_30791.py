import sys

votes = list(map(int, sys.stdin.readline().split()))

sixteenth = votes[0]
res = 0

for i in range(1, len(votes)):
    if sixteenth - votes[i] <= 1000:
        res += 1

print(res)