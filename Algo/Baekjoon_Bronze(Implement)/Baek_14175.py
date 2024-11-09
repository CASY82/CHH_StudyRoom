import sys

m, n, k = map(int, sys.stdin.readline().split())

ori = []
res = []

for _ in range(m):
    ori.append(list(sys.stdin.readline().strip()))

for i in range(m):
    tmp = []
    for j in range(n):
        tmp.append(ori[i][j] * k)
    for z in range(k):
        res.append("".join(tmp))

for r in range(len(res)):
    print(res[r])

# 다른 사람 풀이
# m,n,k = map(int, input().split())
# for _ in range(m):
#     x = input()
#     for i in range(k):
#         for b in x:
#             print(b*k, end='')
#         print()
