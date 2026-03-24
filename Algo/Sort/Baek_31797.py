# 아~파트 아파트
import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())
location = deque([])

for i in range(1, m + 1):
    h1, h2 = map(int, sys.stdin.readline().split())

    location.append((i, h1))
    location.append((i, h2))

tmp = sorted(location, key=lambda x: x[1])
tmp_deque = deque(tmp)

for _ in range(n):
    top = tmp_deque.popleft()
    tmp_deque.append(top)

res = tmp_deque.pop()

print(res[0])