import sys

n, m, p = map(int, sys.stdin.readline().split())
clear = True

for _ in range(n):
    floor = list(map(int, sys.stdin.readline().split()))

    items = floor.count(-1)
    floor.sort()

    for i in range(m):
        if floor[i] == -1:
            continue
        else:
            if floor[i] <= p:
                p += floor[i]
            else:
                while items > 0:
                    p *= 2
                    items -= 1

                    if floor[i] <= p:
                        p += floor[i]
                        break

    # 모든 층을 통과했을때, 아이템 처리
    if i == m - 1 and items > 0:
        p *= (2 ** items)

    if p <= floor[-1]:
        print(0)
        clear = False
        break

if clear:
    print(1)

# 다른 사람 풀이
# import sys
# l = list(map(int, sys.stdin.read().split()))
# n,m,p = l[0], l[1], l[2]
# success = True
# for i in range(3, n*m+3, m):
#     tmp = l[i:i+m]
#     tmp.sort()
#     count = m
#     for j in range(m):
#         if tmp[j] != -1:
#             count = j
#             break
#     for j in range(count, m):
#         if tmp[j] <= p:
#             p += tmp[j]
#         else:
#             while p < tmp[j]:
#                 if count == 0:
#                     success = False
#                     break
#                 count -= 1
#                 p *= tmp[j]
#             p += tmp[j]
#     p *= 2**count
#     if not success:
#         break
# if success:
#     print(1)
# else:
#     print(0)