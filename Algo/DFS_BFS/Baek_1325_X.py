# 답은 맞게 나왔는데 시간초과 ㅠㅠ // pypy로 제출하면 메모리 초과가 나온다 ㅠㅠ
# import sys
# sys.setrecursionlimit(10 ** 6)
#
# n, m = map(int, sys.stdin.readline().split())
#
# adj = [[] for _ in range(n + 1)]
# result = 0
# result_num = set()
#
# #인접 리스트 변형하여 깊이 측정해주고
# for _ in range(m):
#     A, B = map(int, sys.stdin.readline().split())
#
#     adj[B].append(A)
#
# #cnt를 이용해서 깊이 세면 될듯? dfs이용
# def dfs(arr, start, visited):
#     cnt = 1
#
#     for i in arr[start]:
#         if not visited[i]:
#             visited[i] = True
#             cnt += dfs(arr, i, visited)
#
#     return cnt
#
# for i in range(1, n+1):
#     visited = [False for _ in range(n + 1)]
#
#     tmp = dfs(adj, i, visited)
#     if result <= tmp:
#         result = tmp
#         result_num.add(i)
#     else:
#         if i in result_num:
#             result_num.remove(i)
#
# print(*result_num)

# 다른 사람의 풀이를 참고하여 문제 풀이
# 위 풀이랑 로직은 거의 완전 동일하다.
import sys
from collections import deque
from collections import defaultdict

def bfs(start):
    cnt = 1
    visited = [0 for _ in range(n + 1)]
    visited[start] = 1
    queue = deque([start])

    while queue:
        u = queue.popleft()
        for v in computer[u]:
            if not visited[v]:
                queue.append(v)
                visited[v] = 1
                cnt += 1

    return cnt

n, m = map(int, sys.stdin.readline().split())
# 딕셔너리 사용은 좀 신박했다.
computer = defaultdict(list)

for _ in range(m):
    A, B = map(int, sys.stdin.readline().split())

    computer[B].append(A)

result = []
max_cnt = 0

for i in range(1, n+1):
    cnt = bfs(i)
    if cnt > max_cnt:
        max_cnt = cnt
    result.append([i, cnt])

for i, cnt in result:
    if cnt == max_cnt:
        print(i, end = ' ')