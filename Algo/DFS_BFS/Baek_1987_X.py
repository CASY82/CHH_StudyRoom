# 무슨짓을 해도 시간 초과
# import sys
# sys.setrecursionlimit(10 ** 5)
#
# r, c = map(int, sys.stdin.readline().split())
# word = []
# word_tmp = []
# cnt = [0]
# alpha = "A,B,C,D,E,F,G,H,I,J,K,L,M,N,O,P,Q,R,S,T,U,V,W,X,Y,Z".split(",")
# alphaCount = [0 for i in range(26)]
# dx = [-1, 1, 0, 0]
# dy = [0, 0, -1, 1]
#
#
# for i in range(r):
#     word.append(list(sys.stdin.readline().strip()))
#
# def backtrack(x, y):
#
#     if alphaCount[alpha.index(word[y][x])] == 1:
#         cnt[0] = max(cnt[0], alphaCount.count(1))
#         return
#
#     else:
#         alphaCount[alpha.index(word[y][x])] += 1
#
#         for i in range(4):
#             nx = x + dx[i]
#             ny = y + dy[i]
#
#             if nx < 0 or ny < 0 or nx >= c or ny >= r:
#                 continue
#
#             backtrack(nx, ny)
#         alphaCount[alpha.index(word[y][x])] -= 1
#
# backtrack(0, 0)
# print(cnt[0])

# import sys
# sys.setrecursionlimit(10 ** 5)
#
# r, c = map(int, sys.stdin.readline().split())
# word = []
# word_tmp = []
# cnt = [0]
#
# for i in range(r):
#     word.append(list(sys.stdin.readline().strip()))
#
# def backtrack(x, y):
#     dx = [-1, 1, 0, 0]
#     dy = [0, 0, -1, 1]
#
#     if word[y][x] in word_tmp:
#         cnt[0] = max(cnt[0], len(word_tmp))
#         return
#
#     else:
#         word_tmp.append(word[y][x])
#
#         for i in range(4):
#             nx = x + dx[i]
#             ny = y + dy[i]
#
#             if nx < 0 or ny < 0 or nx >= c or ny >= r:
#                 continue
#
#             backtrack(nx, ny)
#         word_tmp.pop()
#
# backtrack(0, 0)
# print(cnt[0])

# 이 참고한 예제도 시간초과 났다....
# import sys
# sys.setrecursionlimit(10 ** 5)
#
# r, c = map(int, sys.stdin.readline().split())
# word = []
# word_set = set()
# result = 0
# dx = [-1, 1, 0, 0]
# dy = [0, 0, -1, 1]
#
# for _ in range(r):
#     word.append(list(sys.stdin.readline().strip()))
#
# def backtrack(x, y, count):
#     global result
#     result = max(count, result)
#
#     for k in range(4):
#         nx = x + dx[k]
#         ny = y + dy[k]
#
#         if 0 <= nx < c and 0 <= ny < r and not word[ny][nx] in word_set:
#             word_set.add(word[ny][nx])
#             backtrack(nx, ny, count + 1)
#             word_set.remove(word[ny][nx])
#
# word_set.add(word[0][0])
# backtrack(0, 0, 1)
# print(result)

#BFS로도 풀수 있을거라고 생각했는데... 그냥 이걸로 할 걸 그랬다.

import sys

# 좌, 하, 우, 상
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]


def BFS(x, y):
    global answer
    q = set([(x, y, board[x][y])])

    while q:
        x, y, ans = q.pop()

        # 좌우상하 갈 수 있는지 살펴본다
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            # index 벗어나지 않는지 체크하고, 새로운 칸이 중복되는 알파벳인지 체크한다
            if ((0 <= nx < R) and (0 <= ny < C)) and (board[nx][ny] not in ans):
                q.add((nx,ny,ans + board[nx][ny]))
                answer = max(answer, len(ans)+1)


R, C = map(int, sys.stdin.readline().split())
board = [list(sys.stdin.readline().strip()) for _ in range(R)]

answer = 1
BFS(0, 0)
print(answer)

#시간이 엄청 짧은 코드. 로직 자체는 동일하나 굉장히 신박한 풀이다!
# from collections import deque
#
# r, c = map(int, input().split())
# graph = [input() for _ in range(r)]
# check = [[set() for _ in range(c)] for _ in range(r)]
# answer = 0
#
# def is_vaild_coord(y, x):
#     return 0 <= y < r and 0 <= x < c
#
# queue = deque()
# check[0][0].add(graph[0][0])
# queue.append((0, 0, graph[0][0]))
#
# dx = (1, 0, -1, 0)
# dy = (0, 1, 0, -1)
#
# while queue:
#     y, x, s = queue.popleft()
#     answer = max(answer, len(s))
#
#     for i in range(4):
#         ny = y + dy[i]
#         nx = x + dx[i]
#         if is_vaild_coord(ny, nx) and graph[ny][nx] not in s:
#             ns = s + graph[ny][nx]
#             if ns not in check[ny][nx]:
#                 check[ny][nx].add(ns)
#                 queue.append((ny, nx, ns))
# print(answer)