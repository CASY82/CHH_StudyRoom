import sys
from collections import deque

n = int(sys.stdin.readline())
result = []
tmp = list(map(int, sys.stdin.readline().split()))
circle_queue = deque()

for i in range(len(tmp)):
    circle_queue.append((tmp[i], i + 1))

while True:
    move, loc = circle_queue.popleft()
    result.append(loc)

    if len(circle_queue) == 0:
        break

    if move > 0:
        move -= 1
        for _ in range(move):
            circle_queue.append(circle_queue.popleft())
    else:
        move = abs(move)
        for _ in range(move):
            circle_queue.appendleft(circle_queue.pop())

print(*result)

# 다른 사람 풀이
# import sys
# input = sys.stdin.readline
# from collections import deque
#
# n = int(input())
# balloons = deque(enumerate(map(int, input().split())))
# ans = []
#
# while balloons:
#     idx, paper = balloons.popleft()
#     ans.append(idx + 1)
#
#     if paper > 0:
#         balloons.rotate(-(paper - 1))
#     elif paper < 0:
#         balloons.rotate(-paper)
#
# print(' '.join(map(str, ans)))