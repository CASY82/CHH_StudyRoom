import sys

n = int(sys.stdin.readline())

max_score = 100
tmp = max_score

for _ in range(n):
    item = int(sys.stdin.readline())

    tmp += item

    if max_score < tmp:
        max_score = tmp

print(max_score)