import sys
from collections import deque
sys.setrecursionlimit(10 ** 5)

MAX = 10 ** 5

n, k = map(int, sys.stdin.readline().split())
limit = [-1 for _ in range(MAX + 1)]
root = [-1 for _ in range(MAX + 1)]
limit[n] = 0
root[n] = n
result = []

def bfs(n):
    loc = deque()
    loc.append(n)

    while loc:
        x = loc.popleft()

        if x == k:
            return

        for nx in (x-1, x+1, x*2):
            if 0 <= nx < (MAX + 1):
                if limit[nx] == -1:
                    limit[nx] = limit[x] + 1
                    root[nx] = x
                    loc.append(nx)

# 여기서 재귀했는데 recursion error... 그래서 for문으로 변경
def path(x):
    temp = x
    for _ in range(limit[x] + 1):
        result.append(temp)
        temp = root[temp]

bfs(n)
path(k)
result.reverse()

print(limit[k])
print(*result)