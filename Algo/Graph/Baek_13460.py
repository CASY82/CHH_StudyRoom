from collections import deque
import sys

input = sys.stdin.readline

N, M = map(int, input().split())
board = [list(input().rstrip()) for _ in range(N)]

# 방향: 상, 하, 좌, 우
dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]

rx = ry = bx = by = -1
for i in range(N):
    for j in range(M):
        if board[i][j] == 'R':
            rx, ry = i, j
            board[i][j] = '.'
        elif board[i][j] == 'B':
            bx, by = i, j
            board[i][j] = '.'

def roll(x, y, dx, dy):
    """해당 방향으로 벽이나 구멍을 만날 때까지 굴린다.
    return: (nx, ny, moved_steps, in_hole)
    """
    steps = 0
    while True:
        nx, ny = x + dx, y + dy
        if board[nx][ny] == '#':
            break
        x, y = nx, ny
        steps += 1
        if board[x][y] == 'O':
            return x, y, steps, True
    return x, y, steps, False

def bfs():
    visited = [[[[False]*M for _ in range(N)] for __ in range(M)] for ___ in range(N)]
    q = deque()
    q.append((rx, ry, bx, by, 0))
    visited[rx][ry][bx][by] = True

    while q:
        crx, cry, cbx, cby, d = q.popleft()
        if d >= 10:  # 더 기울이면 11회 이상이므로 중단
            continue

        for dx, dy in dirs:
            nrx, nry, rsteps, rHole = roll(crx, cry, dx, dy)
            nbx, nby, bsteps, bHole = roll(cbx, cby, dx, dy)

            # 파란이 빠지면 실패 가지치기
            if bHole:
                continue
            # 빨간만 빠지면 성공
            if rHole and not bHole:
                return d + 1

            # 같은 칸에 멈춘 경우(구멍 아님) => 더 멀리 간 공을 한 칸 뒤로
            if nrx == nbx and nry == nby:
                if rsteps > bsteps:
                    nrx -= dx
                    nry -= dy
                else:
                    nbx -= dx
                    nby -= dy

            if not visited[nrx][nry][nbx][nby]:
                visited[nrx][nry][nbx][nby] = True
                q.append((nrx, nry, nbx, nby, d + 1))

    return -1

print(bfs())
