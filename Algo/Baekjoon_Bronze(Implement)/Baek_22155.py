import sys

n = int(sys.stdin.readline())

for _ in range(n):
    i, f = map(int, sys.stdin.readline().split())

    if (i < 2 and f < 3) or (i < 3 and f < 2):
        print("Yes")
    else:
        print("No")

# 다른 사람 풀이
# t=int(input())
# for _ in range(t):
#     n,m=map(int,input().split())
#     if n<=1 and m<=2 or n<=2 and m<=1:
#         print('Yes')
#     else:
#         print('No')