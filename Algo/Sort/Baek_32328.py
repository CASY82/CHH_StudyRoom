import sys

n = int(sys.stdin.readline())
scores = []

for _ in range(n):
    scores.append(int(sys.stdin.readline()))

tmp = list(set(scores))
tmp.sort(reverse=True)
res = tmp[2]
cnt = scores.count(tmp[2])
print(res, cnt)