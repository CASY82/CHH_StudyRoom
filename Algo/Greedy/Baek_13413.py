import sys

t = int(sys.stdin.readline())

for _ in range(t):
    n = int(sys.stdin.readline())

    now = list(sys.stdin.readline().strip())
    target = list(sys.stdin.readline().strip())
    stack = []
    cnt = 0

    for i in range(len(now)):
        if now[i] != target[i]:
            stack.append(now[i])

    Bcnt = stack.count('B')
    Wcnt = stack.count('W')
    cnt = max(Bcnt, Wcnt)

    print(cnt)