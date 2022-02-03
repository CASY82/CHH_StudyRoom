import sys

n = int(sys.stdin.readline())

num = [i+1 for i in range(n+1)]
location = [0 for i in range(n)]
check = [True for i in range(n)]

def backtrack(v):
    if v == n:
        for i in location:
            print(i, end=" ")
        print()

    else:
        for j in range(n):
            if check[j]:
                check[j] = False
                location[v] = num[j]
                backtrack(v+1)
                location[v] = 0
                check[j] = True

backtrack(0)