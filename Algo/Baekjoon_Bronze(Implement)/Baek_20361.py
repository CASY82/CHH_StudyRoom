import sys

n, x, k = map(int, sys.stdin.readline().split())

loc = [0 for _ in range(n)]

loc[x-1] = 1

for i in range(k):
    a, b = map(int, sys.stdin.readline().split())

    loc[a-1], loc[b-1] = loc[b-1], loc[a-1]

print(loc.index(1)+1)

#다른 사람 풀이
# n,x,k = map(int,input().split())
# for i in range(k):
#     a , b = map(int,input().split())
#     if a==x:
#         x = b
#     elif b==x:
#         x = a
# print(x)