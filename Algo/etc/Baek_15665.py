import sys

n, m = map(int, sys.stdin.readline().split())
num = list(map(int, sys.stdin.readline().split()))

num.sort()
locate = [''] * m

def backtrack(x):
    if x == m+1:
        print(' '.join(locate))

    else:
        overlap = 0
        for i in range(1, n+1):
            if overlap != num[i - 1]:
                locate[x - 1] = str(num[i - 1])
                overlap = num[i - 1]
                backtrack(x + 1)
                locate[x - 1] = ''

backtrack(1)