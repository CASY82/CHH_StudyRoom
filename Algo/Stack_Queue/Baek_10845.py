import sys
from collections import deque
n = int(sys.stdin.readline())
que = deque()

for _ in range(n):

    word = list(sys.stdin.readline().strip().split())

    if word[0] == 'push':
        que.append(int(word[1]))

    if word[0] == 'front':
        if not que:
            print(-1)
        else:
            print(que[0])

    if word[0] == 'size':
        print(len(que))

    if word[0] == 'empty':
        if que:
            print(0)
        else:
            print(1)

    if word[0] == 'back':
        if not que:
            print(-1)
        else:
            print(que[-1])

    if word[0] == 'pop':
        if not que:
            print(-1)
        else:
            print(que.popleft())
