from collections import deque

# n = 5
# edges = [[0,1],[0,2],[1,3],[1,4]]

n = 4
edges = [[2,3],[0,1],[1,2]]


def bfs(start, n, adj):
    que = deque()
    que.append((start, 0))
    visited = [True for i in range(n)]
    visited[start] = False
    cnt = 0

    while que:
        num, depth = que.popleft()

        if depth >= 2:
            cnt += len(adj[num])

        for i in adj[num]:
            if visited[i]:
                visited[i] = False
                que.append((i, depth+1))

    return cnt


def solution(n, edges):
    answer = 0

    adj = [[] for _ in range(n)]

    #인접 리스트
    for i in range(len(edges)):
        src, dest = edges[i][0], edges[i][1]

        adj[src].append(dest)
        adj[dest].append(src)

    print(adj)

    #인접 리스트를 이용해서 연결된 노드의 모든 순서쌍을 구하기
    #중간 노드 개수를 세고 중간노드가 가진 하위 노드의 개수를 세서 더한다
    for i in range(n):
        answer += bfs(i, n, adj)

    return answer

print(solution(n, edges))