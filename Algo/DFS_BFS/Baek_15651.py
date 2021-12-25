import sys

n, m = map(int, sys.stdin.readline().split())

locate = [0] * (m+1)

def backtrack(x):
    if x == m+1:
        for i in range(1, m+1):
            print(locate[i], end=' ')
        print()

    else:
        for j in range(1, n+1):
            locate[x] = j
            backtrack(x + 1)
            locate[x] = 0

backtrack(1)