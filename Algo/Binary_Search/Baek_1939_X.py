# bfs에 대한 이해도가 낮아서 해당 내용은 참고하여 풀어냈음. dfs/bfs를 좀더 연습할 필요가 있다.
import sys
from collections import deque

#인접한 섬을 세야하므로 bfs
def bfs(mid):
    #시작 공장 방문 처리
    visit[factory_fir] = 1
    queue = deque()
    queue.append(factory_fir)

    while queue:
        st = queue.popleft()
        #수를 뽑았는데 도착 공장이면 바로 True 반환
        if st == factory_sec:
            return True
        #아니라면 방문하지 않은 섬들을 지나면서 도착 공장이 나올때까지 큐에 입력 후 방문처리
        for nx, nc in bridge[st]:
            if visit[nx] == 0 and mid <= nc:
                queue.append(nx)
                visit[nx] = 1

    return False

n, m = map(int, sys.stdin.readline().split())
bridge = [[] for _ in range(n+1)]

#인접 리스트
for _ in range(m):
    src, dest, c = map(int, sys.stdin.readline().split())
    bridge[src].append([dest, c])
    bridge[dest].append([src, c])

factory_fir, factory_sec = map(int, sys.stdin.readline().split())

start = 1
end = 1000000000

#이분 탐색
while start <= end:
    visit = [0 for _ in range(n+1)]
    mid = (start + end) // 2

    #mid값은 중량이므로 중량값을 기준으로 방문판단
    if bfs(mid):
        start = mid + 1
    else:
        end = mid - 1

print(end)