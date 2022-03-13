import sys
from collections import deque

n, k = map(int, sys.stdin.readline().split())
MAX = 10 ** 5
# 왜 -1로 시작해야만 동일하지....?
limit = [[-1, 0] for _ in range(MAX + 2)]
limit[n][0] = 0
limit[n][1] = 1

def bfs(n):
    loc = deque()
    loc.append(n)

    while loc:
        x = loc.popleft()

        for nx in (x-1, x+1, x*2):
            if 0 <= nx < (MAX + 1):
            # 처음 방문하는 경우에는 값을 더해 넣고 방문횟수를 x와 동일하게 맞춰준다.
                if limit[nx][0] == -1:
                    limit[nx][0] = limit[x][0] + 1
                    limit[nx][1] = limit[x][1]
                    loc.append(nx)
                # 이 부분 조건을 잘못 생각하고 있었음 즉, 1번 더 방문한 것과 동일한 경우만 체크하도록 해야했다.
                elif limit[nx][0] == limit[x][0] + 1:
                    limit[nx][1] += limit[x][1]

bfs(n)
print(limit[k][0])
print(limit[k][1])

# 테스트 장소
# import sys
# from collections import deque
#
# n, k = map(int, sys.stdin.readline().split())
# MAX = 30
#  -1로 시작해야만 자기 자신을 부를 때 문제가 없다. 5 5 가 들어오면  0 1로 결과가 나오게 된다.
# limit = [[-1, 0] for _ in range(MAX + 2)]
# limit[n][0] = 0
# limit[n][1] = 1
#
# def bfs(n):
#     loc = deque()
#     loc.append(n)
#
#     while loc:
#         x = loc.popleft()
#
#         for nx in (x-1, x+1, x*2):
#             if 0 <= nx < (MAX + 1):
#             # 처음 방문하는 경우에는 값을 더해 넣고 방문횟수를 x와 동일하게 맞춰준다.
#                 if limit[nx][0] == -1:
#                     limit[nx][0] = limit[x][0] + 1
#                     limit[nx][1] = limit[x][1]
#                     loc.append(nx)
#                 # 이 부분 조건을 잘못 생각하고 있었음 즉, 1번 더 방문한 것과 동일한 경우만 체크하도록 해야했다.
#                 elif limit[nx][0] == limit[x][0] + 1:
#                     limit[nx][1] += limit[x][1]
#
# bfs(n)
# print(limit[k][0])
# print(limit[k][1])
# print(limit)

#
# import sys
# from collections import deque
#
# n, k = map(int, sys.stdin.readline().split())
# MAX = 30
# 자기 자신을 부를 때 즉, 5 5 입력이 들어오면 다른 개체에 의해서 횟수가 세어져 버리므로 2 , 2가 나오면서 문제발생
# limit = [[0, 0] for _ in range(MAX + 2)]
# # limit[n][0] = 0
# limit[n][1] = 1
#
# def bfs(n):
#     loc = deque()
#     loc.append(n)
#
#     while loc:
#         x = loc.popleft()
#
#         for nx in (x-1, x+1, x*2):
#             if 0 <= nx < (MAX + 1):
#             # 처음 방문하는 경우에는 값을 더해 넣고 방문횟수를 x와 동일하게 맞춰준다.
#                 if limit[nx][0] == 0:
#                     limit[nx][0] = limit[x][0] + 1
#                     limit[nx][1] = limit[x][1]
#                     loc.append(nx)
#                 # 이 부분 조건을 잘못 생각하고 있었음 즉, 1번 더 방문한 것과 동일한 경우만 체크하도록 해야했다.
#                 elif limit[nx][0] == limit[x][0] + 1:
#                     limit[nx][1] += limit[x][1]
#
# bfs(n)
# print(limit[k][0])
# print(limit[k][1])
# print(limit)