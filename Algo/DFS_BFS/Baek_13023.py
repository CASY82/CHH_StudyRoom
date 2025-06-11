def find_friend_chain(N, graph):
    # DFS로 길이 4인 경로(5명: A->B->C->D->E)를 찾음
    def dfs(v, depth, visited):
        if depth == 4:  # A->B->C->D->E (4개의 간선)
            return True
        for next_v in graph[v]:
            if not visited[next_v]:
                visited[next_v] = True
                if dfs(next_v, depth + 1, visited):
                    return True
                visited[next_v] = False
        return False

    # 모든 노드에서 DFS 시작
    for start in range(N):
        visited = [False] * N
        visited[start] = True
        if dfs(start, 0, visited):
            return 1
    return 0


# 입력 처리
N, M = map(int, input().split())
graph = [[] for _ in range(N)]
for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)  # 양방향 그래프

# 결과 출력
print(find_friend_chain(N, graph))