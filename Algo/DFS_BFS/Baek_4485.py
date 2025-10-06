import heapq
import sys

tc = 1
while True:
    n = int(sys.stdin.readline())

    if n == 0:
        break

    cave = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
    INF = 10 ** 9
    dist = [[INF] * n for _ in range(n)]
    dist[0][0] = cave[0][0]
    pq = [(cave[0][0], 0, 0)]

    direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    while pq:
        cost, r, c = heapq.heappop(pq)

        if cost > dist[r][c]:
            continue
        if r == n - 1 and c == n - 1:
            break

        for dr, dc in direction:
            nr, nc = r + dr, c + dc
            if 0 <= nr < n and 0 <= nc < n:
                ncost = cost + cave[nr][nc]
                if ncost < dist[nr][nc]:
                    dist[nr][nc] = ncost
                    heapq.heappush(pq, (ncost, nr, nc))

    print(f"Problem {tc}: {dist[n-1][n-1]}")
    tc += 1