import sys

n = int(sys.stdin.readline())
rank = []

for _ in range(n):
    rank.append(int(sys.stdin.readline()))

rank.sort()
result = 0

for i in range(len(rank)):
    result += abs(rank[i] - (i+1))

print(result)