import sys

n, m = map(int, sys.stdin.readline().split())

visit = [False]*(n+1)
arr = [0]*(m+1)

def check(x, num):
    if x == m+1:
        for i in range(1, m+1):
            print(arr[i], end=' ')
        print()
    else:
        for i in range(num, n+1):
            if not visit[i]:
                visit[i] = True
                arr[x] = i
                check(x+1, i)
                arr[x] = 0
                visit[i] = False

check(1, 1)