import sys

n, m = map(int, sys.stdin.readline().split())
num = list(map(int, sys.stdin.readline().split()))

num.sort()
locate = [0] * (m+1)

def backtrack(x, sc):
    if x == m + 1:
        for i in range(1, m+1):
            print(locate[i], end=' ')
        print()

    else:
        for j in range(sc, n+1):
            locate[x] = num[j - 1]
            backtrack(x+1, j)
            locate[x] = 0

backtrack(1, 1)