# import sys
# from collections import deque
#
# n = int(sys.stdin.readline())
# stone_bridge = list(map(int, sys.stdin.readline().split()))
# start, end = map(int, sys.stdin.readline().split())
#
# def bfs(start, end):
#     queue = deque()
#     visited = [True for i in range(len(stone_bridge))]
#
#     queue.append((start, 0))
#     visited[start - 1] = False
#
#     while queue:
#         now, cnt = queue.popleft()
#
#         if abs(end - now) % stone_bridge[now-1] == 0:
#             return cnt + 1
#
#         for j in ((end // stone_bridge[now-1]) + now, now - (end // stone_bridge[now-1])):
#             if 0 <= j < len(stone_bridge):
#                 if visited[j]:
#                     queue.append((j, cnt + 1))
#                     visited[j] = False
#
#     return -1
#
# print(bfs(start, end))

from collections import deque

def bfs(a, b, bridge, N):
    q = deque()
    q.append(a-1)
    check = [-1]*N
    check[a-1] = 0
    while q:
        node = q.popleft()
        for n in range(N):
            if (n-node)%bridge[node] == 0 and check[n] == -1:
                q.append(n)
                check[n] = check[node] + 1
                if n == b-1:
                    return check[n]
    return -1

N = int(input())
bridge = list(map(int, input().split()))
a, b = map(int, input().split())
print(bfs(a, b, bridge, N))