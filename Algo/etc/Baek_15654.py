import sys

n, m = map(int, sys.stdin.readline().split())
num = list(map(int, sys.stdin.readline().split()))

num.sort()

check = [False] * (n+1)
locate = [0] * (m+1)

def backtrack(x):
    if x == m + 1:
        for i in range(1, m+1):
            print(locate[i], end=' ')
        print()

    else:
        for j in range(1, n+1):
            if not check[j]:
                check[j] = True
                locate[x] = num[j-1]
                backtrack(x + 1)
                check[j] = False
                locate[x] = 0

backtrack(1)