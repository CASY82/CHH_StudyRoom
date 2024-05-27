import sys

n, k = map(int, sys.stdin.readline().split())
cost_diff = []
over = 0

for _ in range(n):
    ai, bi = map(int, sys.stdin.readline().split())

    if bi - ai > 0:
        cost_diff.append(bi - ai)
    else:
        over += 1

if over >= k:
    print(0)
else:
    tmp = k - over
    cost_diff.sort()

    print(cost_diff[tmp - 1])

# 다른 사람 풀이
# import sys
#
# input=sys.stdin.readline
# N,K=map(int,input().split())
# temp=[]
# for i in range(N):
#     a,b=map(int,input().split())
#     if a>=b:
#         K-=1
#     else:
#         temp.append(a-b)
# sol=0
# temp.sort()
# if K<=0:
#     print(0)
#     exit()
# while K:
#     sol=-temp.pop()
#     K-=1
#
# print(sol)