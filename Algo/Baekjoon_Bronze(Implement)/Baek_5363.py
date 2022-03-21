import sys
from collections import deque

n = int(sys.stdin.readline())

for _ in range(n):
    sentense = list(sys.stdin.readline().strip().split())

    sentense.append(sentense[0])
    sentense.append(sentense[1])

    for i in range(2, len(sentense)):
        print(sentense[i], end=' ')
    print()