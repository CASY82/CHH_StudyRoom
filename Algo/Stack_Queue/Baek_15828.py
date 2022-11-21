import sys
from collections import deque

que = deque()
size = int(sys.stdin.readline())

while True:
    message = int(sys.stdin.readline())

    if message == -1:
        break

    if message == 0:
        que.popleft()
    else:
        if len(que) < size:
            que.append(message)

if len(que) == 0:
    print("empty")
else:
    print(*que)