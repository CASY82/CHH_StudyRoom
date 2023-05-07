import sys

n = int(sys.stdin.readline())

adj = [[] for _ in range(n+1)]

for _ in range(n-1):
    src, dest = map(int, sys.stdin.readline().split())

    adj[src].append(dest)
    adj[dest].append(src)

q = int(sys.stdin.readline())

for _ in range(q):
    t, k = map(int, sys.stdin.readline().split())

    # 단절점 일때는, 노드에 연결된 간선의 개수가 2개면 단절점
    if t == 1:
        if len(adj[k]) >= 2:
            print("yes")
        else:
            print("no")
    # 단절선은 무조건 두 개의 트리로 나눠진다.
    else:
        print("yes")