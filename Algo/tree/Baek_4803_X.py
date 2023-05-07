import sys
sys.setrecursionlimit(300000)

def dfs(graph, v, visit, parent):
    # 이미 한번 방문했던 노드에 다시 도달했을때
    if not visit[v]:
        return False

    visit[v] = False

    # 기존 인접 행렬 노드 순회에서, 부모 체크 로직이 추가 되었다.
    for node in graph[v-1]:
        # 부모 노드 연결 확인
        if node != parent:
            # 자식 노드를 방문했는데, 이미 방문한 자식(즉, 사이클이다)
            if not dfs(graph, node, visit, v):
                return False

    return True

case = 0
while True:
    case += 1
    n, m = map(int, sys.stdin.readline().split())
    result = 0

    if n == 0 and m == 0:
        break

    adj = [[] for _ in range(n)]

    for i in range(m):
        src, dest = map(int, sys.stdin.readline().split())

        adj[src-1].append(dest)
        adj[dest-1].append(src)

    visited = [True for _ in range(n+1)]

    for i in range(1, n+1):
        # 방문했던 노드라면 수행할 필요가 없다.(즉, 하나의 트리에 있다)
        if not visited[i]:
            continue
        # 방문하지 않았다면 DFS를 수행해서 트리 방문 수행을 진행한다.
        if dfs(adj, i, visited, 0):
            result += 1

    if result == 0:
        print("Case {}: No trees.".format(case))
    elif result == 1:
        print("Case {}: There is one tree.".format(case))
    else:
        print("Case {0}: A forest of {1} trees.".format(case, result))