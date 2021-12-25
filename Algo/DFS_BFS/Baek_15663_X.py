#시간초과로 고생하다가 overlap이라는 변수의 활용법을 알고난 뒤로 성공하였다.

import sys

n, m = map(int, sys.stdin.readline().split())
num = list(map(int, sys.stdin.readline().split()))

num.sort()
check = [False] * (n+1)
locate = [' '] * m
result = []

def backtrack(x):
    if x == m+1:
        print(' '.join(locate))

    else:
        overlap = 0
        for j in range(1, n+1):
            if not check[j] and overlap != num[j-1]:
                check[j] = True
                locate[x-1] = str(num[j-1])
                overlap = num[j-1]
                backtrack(x + 1)
                check[j] = False
                locate[x-1] = 0

backtrack(1)
