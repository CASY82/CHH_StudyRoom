# 아니 왜 시간초과임? --> 해결
# 0 - 1 BFS는 참고할 것 이 문제는 단순 BFS로도 풀리는 문제여서 다행이다.
import sys
from collections import deque

n, k = map(int, sys.stdin.readline().split())
#이 부분... 실수;;; 25000값이 곱해지는 과정에서 문제 발생;;;;(ex : 25000 100000)
MAX = 10 ** 5 + 1
# 이 부분이 0이면 시간초과 발생!!! 아무래도 0인 경우를 전부 que에 넣다보니 발생하는게 아닌가 싶다.
limit = [-1] * MAX
limit[n] = 0

def bfs():
    que = deque()
    que.append(n)

    while que:
        x = que.popleft()
        # print("x : ", x)

        if x == k:
            print(limit[k])
            return

        if 0 <= x*2 < MAX and limit[x*2] == -1:
            # print('x*2 : ', x*2)
            limit[x*2] = limit[x]
            que.appendleft(x*2)

        for nx in (x-1, x+1):
            if 0 <= nx < MAX and limit[nx] == -1:
                # print('nx : ', nx)
                limit[nx] = limit[x] + 1
                que.append(nx)

bfs()
# print(limit)

# import sys
# from collections import deque
#
# n, k = map(int, sys.stdin.readline().split())
# MAX = 10 ** 5 + 1
# limit = [-1] * MAX
# limit[n] = 0
#
# def bfs():
#     que = deque()
#     que.append(n)
#
#     while que:
#         x = que.popleft()
#
#         if x == k:
#             print(limit[k])
#             return
#
#         for nx in (2*x, x-1, x+1):
#             if 0 <= nx < MAX and limit[nx] == -1:
#                 if nx == 2*x:
#                     limit[nx] = limit[x]
#                     que.appendleft(nx)
#
#                 else:
#                     limit[nx] = limit[x] + 1
#                     que.append(nx)
#
# bfs()