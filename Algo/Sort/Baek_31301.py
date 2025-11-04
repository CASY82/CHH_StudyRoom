import sys
from collections import defaultdict

n, k, c = map(int, sys.stdin.readline().split())
school = defaultdict(int)
res = []
tmp = []

for score in range(1, n + 1):
    t, s = map(int, sys.stdin.readline().split())

    if school[s] < c and len(res) < k:
        res.append((t, score))
        school[s] += 1
    else:
        tmp.append((t, score))

if len(res) < k:
    for i in range(k - len(res)):
        res.append(tmp[i])

res.sort(key=lambda x:x[1])

for id, rank in res:
    print(id)