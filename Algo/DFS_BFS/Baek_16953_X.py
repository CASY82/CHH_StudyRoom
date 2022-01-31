# bfs를 이용해서 구하는 문제 bfs를 크게 다뤄본적이 없어서 일단 참고하여 진행하였다.
import sys
from collections import deque

a, b = map(int, sys.stdin.readline().split())
result = -1
queue = deque([(a, 1)])

while queue:
    num, cnt = queue.popleft()

    if num == b:
        result = cnt
        break

    # 2배한 경우 넣기
    if num * 2 <= b:
        queue.append((num * 2, cnt + 1))
    # 뒤에 1붙인 경우 넣기
    if num * 10 + 1 <= b:
        queue.append((num * 10 + 1, cnt + 1))

print(result)