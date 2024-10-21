import sys

t = int(sys.stdin.readline())
package = [0, 0, 0]

for _ in range(t):
    a, b, c = map(int, sys.stdin.readline().split())

    package[0] += a
    package[1] += b
    package[2] += c

    min_cnt = min(package)

    if min_cnt < 30:
        print("NO")
    else:
        print(min_cnt)
        for i in range(3):
            package[i] -= min_cnt

# 다른 사람 풀이
# def s():
#     n,*r=map(int,open(0).read().split())
#     a=[0]*3
#     for i in range(0,n*3,3):
#         a=[r[i+j]+x for j,x in enumerate(a)]
#         mn=min(a)
#         if mn>=30:
#             print(mn)
#             a=[k-mn for k in a]
#         else:
#             print('NO')
# s()