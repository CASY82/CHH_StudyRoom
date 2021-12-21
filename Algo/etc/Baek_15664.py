import sys

n, m = map(int, sys.stdin.readline().split())
num = list(map(int, sys.stdin.readline().split()))

num.sort()
check = [False] * (n+1)
locate = [' '] * m

def backtrack(x, sn):
    if x == m + 1:
        print(' '.join(locate))

    else:
        overlap = 0
        for j in range(sn, n+1):
            if not check[j] and overlap != num[j - 1]:
                check[j] = True
                locate[x-1] = str(num[j - 1])
                overlap = num[j - 1]
                backtrack(x + 1, j)
                locate[x - 1] = ' '
                check[j] = False

backtrack(1, 1)