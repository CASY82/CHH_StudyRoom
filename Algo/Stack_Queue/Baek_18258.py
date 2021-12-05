# deque를 안쓰고 풀어보려했으나 시간 초과....
# import sys
# n = int(sys.stdin.readline())
# queue = []
#
# for _ in range(n):
#     command = list(sys.stdin.readline().rstrip().split())
#
#     if command[0] == 'push':
#         queue.append(command[1])
#
#     if command[0] == 'front':
#         if queue:
#             print(queue[0])
#         else:
#             print(-1)
#
#     if command[0] == 'back':
#         if queue:
#             print(queue[len(queue) - 1])
#         else:
#             print(-1)
#
#     if command[0] == 'pop':
#         if queue:
#             print(queue.pop(0)) # 이친구가 굉장히 시간을 오래 잡아먹게하는 주범...
#         else:
#             print(-1)
#
#     if command[0] == 'size':
#         print(len(queue))
#
#     if command[0] == 'empty':
#         if queue:
#             print(0)
#         else:
#             print(1)

from collections import deque
import sys
n = int(sys.stdin.readline())
queue = deque()

for _ in range(n):
    command = list(sys.stdin.readline().rstrip().split())

    if command[0] == 'push':
        queue.append(command[1])

    if command[0] == 'front':
        if queue:
            print(queue[0])
        else:
            print(-1)

    if command[0] == 'back':
        if queue:
            print(queue[len(queue) - 1])
        else:
            print(-1)

    if command[0] == 'pop':
        if queue:
            print(queue.popleft())
        else:
            print(-1)

    if command[0] == 'size':
        print(len(queue))

    if command[0] == 'empty':
        if queue:
            print(0)
        else:
            print(1)