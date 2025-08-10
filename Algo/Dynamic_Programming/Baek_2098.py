import sys
from functools import lru_cache
sys.setrecursionlimit(1 << 25)

n = int(sys.stdin.readline())
w = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

inf = 10 ** 15
all = (1 << n) - 1
start = 0

@lru_cache(maxsize=None)
def dp(mask, u):
    # 모든 도시 방문 완료 -> 시작점으로 돌아감
    if mask == all:
        return w[u][start] if w[u][start] > 0 else inf

    ans = inf

    # 다음 도시 v로 이동
    for v in range(n):
        if (mask >> v) & 1:
            continue
        if w[u][v] == 0:
            continue
        cost = w[u][v] + dp(mask | (1 << v), v)

        if cost < ans:
            ans = cost

    return ans

print(dp(1 << start, start))