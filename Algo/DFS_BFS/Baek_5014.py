# 너무 무식한 방법 일단 bfs의 적용은 성공적이었으나... 예외 조건 처리를 어떻게 할지 전혀 감이 안잡힘
# import sys
# from collections import deque
#
# f, s, g, u, d = map(int, sys.stdin.readline().split())
#
# visited = [False] * (f+1)
# que = deque()
# que.append((s, 0))
# visited[s] = True
# result = 0
#
# if g == s:
#     print(result)
# elif d == 0 and u == 0 and g != s:
#     print("use the stairs")
# elif d == 0 and u == 0 and g == s:
#     print(result)
# elif s + u > f and s - d < 1:
#     print("use the stairs")
# elif u == 0 and g > s:
#     print("use the stairs")
# elif d == 0 and g < s:
#     print("use the stairs")
# elif u == 0 and (g-s)%d != 0:
#     print("use the stairs")
# elif d == 0 and (g-s)%u != 0:
#     print("use the stairs")
# elif d == u and (g-s)%u != 0:
#     print("use the stairs")
# else:
#     while que:
#         floor, cnt = que.popleft()
#
#         if floor == g:
#             result = cnt
#             break
#
#         if floor + u <= f and not visited[floor + u]:
#             visited[floor + u] = True
#             que.append((floor+u, cnt+1))
#
#         if floor - d > 0 and not visited[floor - d]:
#             visited[floor - d] = True
#             que.append((floor-d, cnt+1))
#
#     print(result)

from collections import deque
import sys

f, s, g, u, d = map(int, sys.stdin.readline().split())
button = [u, -d]
#dp를 이용하는 문제였나보다. 이 부분을 통해서 도착하지 못한곳들은 -1로 남게 된다.
stair_check = [-1 for i in range(f + 1)]
stair_check[s] = 0

def bfs(num):
    que = deque()
    que.append(num)
    visited = [True for i in range(f+1)]
    visited[num] = False

    while que:
        x = que.popleft()
        for i in range(2):
            nx = x + button[i]
            if 0 < nx <= f and visited[nx]:
                que.append(nx)
                #이 부분에서 해당 층을 몇번째에 도착하는지 체크하게 된다.
                stair_check[nx] = stair_check[x] + 1
                visited[nx] = False

bfs(s)
print(stair_check[g] if stair_check[g] != -1 else "use the stairs")