import sys
from collections import deque

n = int(sys.stdin.readline())

for _ in range(n):
    num = list(sys.stdin.readline().strip())
    num = deque(num)

    result = True
    while num:
        front = num.popleft()
        end = num.pop()

        if front == end:
            result = True
        else:
            result = False

    if result:
        print("Do-it")
    else:
        print("Do-it-Not")