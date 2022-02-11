# 메모리 초과
# import sys
# from collections import deque
#
# n, k = map(int, sys.stdin.readline().split())
# loc = deque([(n, 0)])
# result = 0
#
# while loc:
#     now, cnt = loc.popleft()
#
#     if now == k:
#         result = cnt
#         break
#
#     if now - 1 <= k:
#         loc.append((now - 1, cnt + 1))
#
#     if now + 1 <= k:
#         loc.append((now + 1, cnt + 1))
#
#     if now * 2 <= k:
#         loc.append((now * 2, cnt + 1))
#
# print(result)

import sys
from collections import deque

n, k = map(int, sys.stdin.readline().split())
MAX = 10 ** 5
limit = [0] * (MAX + 1)

def bfs():
    loc = deque()
    loc.append(n)

    while loc:
        x = loc.popleft()

        # x값이 위치 이므로 해당 값과 동생의 위치가 같으면 멈춤
        if x == k:
            print(limit[x])
            break

        #이런식으로 사용이 가능하다는 건 처음알았다....
        for nx in (x-1, x+1, x*2):
            #메모리 초과를 방지하기 위해서 리스트를 제한
            if 0 <= nx <= MAX and not limit[nx]:
                limit[nx] = limit[x] + 1
                loc.append(nx)

bfs()