# DFS로 구현해봤는데 몇몇 테스트 케이스는 돌아가지 않는 현상을 보였으며, 예제만 맞고 있길래 그냥 조합 공식을 이용하여 풀기로 했다.
# import sys
# sys.setrecursionlimit(10 ** 5)
#
# n, s = map(int, sys.stdin.readline().split())
# num = list(map(int, sys.stdin.readline().split()))
#
# visited = [False] * (n+1)
# result = []
# bubun = []
#
# print(num)
#
# def backtrack(v):
#     if v > n:
#         return
#     if sum(result) == s and result:
#         bubun.append(result)
#
#     else:
#         for i in range(len(num)):
#             if not visited[i]:
#                 visited[i] = True
#                 result.append(num[i])
#                 backtrack(v + 1)
#                 visited[i] = False
#                 result.pop()
#
# backtrack(0)
#
# print(bubun)
# print(len(bubun))

import sys
from itertools import combinations

n, s = map(int, sys.stdin.readline().split())
num = list(map(int, sys.stdin.readline().split()))
cnt = 0

for i in range(1, n+1):
    result = list(combinations(num, i))

    for j in result:
        if s == sum(list(j)):
            cnt += 1

print(cnt)

#시간은 오래걸리지만 DFS(백트래킹)로 구현한 예제 --> 자바는 이 공식으로 풀면 되겠다.
# import sys
# sys.setrecursionlimit(10**8)
#
#
# def dfs(start: int):
#     global visited, ans
#
#     for i in range(start, N):
#         if visited[i]:
#             continue
#         visited[i] = str(seq[i])
#         dfs(i)
#
#         if sum(map(int, visited)) == S:
#             ans += 1
#
#         visited[i] = 0
#
#     return
#
#
# N, S = map(int, input().split())
# seq = list(map(int, input().split()))
# visited = [0] * N  # 방문 여부 체크
# ans = 0
#
# dfs(0)
#
# print(ans)