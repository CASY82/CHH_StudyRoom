# 인접 행렬
# 그래프 간의 관계를 알아보기에 좋다. 노드의 개수가 간선의 개수보다 많으면 많을수록 탐색을 위해 소요되는 시간이 증가 즉 "노드 수 < 간선 수" 일때 사용하면 효과적
# import sys
#
# node, edge = map(int, sys.stdin.readline().split())
#
# adj = [[0 for _ in range(node)] for _ in range(node)]
#
# print(adj)
# for _ in range(edge):
#     src, dest = map(int, sys.stdin.readline().split())
#
#     adj[src-1][dest-1] = 1
#     adj[dest-1][src-1] = 1
#
#     print(adj)

#예제 출력 예
# [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
# [[0, 1, 0, 0], [1, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
# [[0, 1, 1, 0], [1, 0, 0, 0], [1, 0, 0, 0], [0, 0, 0, 0]]
# [[0, 1, 1, 1], [1, 0, 0, 0], [1, 0, 0, 0], [1, 0, 0, 0]]
# [[0, 1, 1, 1], [1, 0, 1, 0], [1, 1, 0, 0], [1, 0, 0, 0]]
# [[0, 1, 1, 1], [1, 0, 1, 0], [1, 1, 0, 1], [1, 0, 1, 0]]


#인접 리스트
# import sys
#
# node, edge = map(int, sys.stdin.readline().split())
#
# adj = [[] for _ in range(node)]
# print(adj)
#
# for _ in range(edge):
#     src, dest = map(int, sys.stdin.readline().split())
#     adj[src-1].append(dest)
#     adj[dest-1].append(src)
#
#     print(adj)

# 예제 출력 예
# [[], [], [], []]
# [[2], [1], [], []]
# [[2, 3], [1], [1], []]
# [[2, 3, 4], [1], [1], [1]]
# [[2, 3, 4], [1, 3], [1, 2], [1]]
# [[2, 3, 4], [1, 3], [1, 2, 4], [1, 3]]

#예제
# 4 5
# 1 2
# 1 3
# 1 4
# 2 3
# 3 4