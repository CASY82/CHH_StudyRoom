import sys
from collections import deque

n = int(sys.stdin.readline())
numList = deque()

for _ in range(n):
    numList.append(int(sys.stdin.readline()))

i = 1
tmp = []
result = []

while numList:
    check = True

    if tmp and numList[0] == tmp[-1]:
        numList.popleft()
        tmp.pop()
        check = False
    else:
        tmp.append(i)

    if check:
        result.append('+')
        if i <= n:
            i += 1
        else:
            print("NO")
            break
    else:
        result.append('-')

if not numList:
    for i in result:
        print(i)