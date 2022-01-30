# import sys
#
# n = int(sys.stdin.readline())
# antena = list(map(int, sys.stdin.readline().split()))
#
# antena.sort()
# # min = 100001
# 브루트 포스, 소트하는 의미가 없다. 아마 시간초과일것
# for i in antena:
#     sumRange = 0
#     for j in range(n):
#         sumRange += abs(antena[j] - i)
#     if min > sumRange:
#         min = sumRange
#         result = i

# import sys
# from collections import Counter
#
# n = int(sys.stdin.readline())
# antena = list(map(int, sys.stdin.readline().split()))
#
# antena.sort()

#가장 개수가 많은 수 중 작은애 pick 할필요 없다;;;;
# countNum = Counter(antena)
#
# result = list(countNum.most_common())
# result = sorted(result, key=lambda x:(-x[1], x[0]))

# 개수가 동일하다면 가운데(짝수일땐 가운데 두 수중 작은놈)

# if result[0][1] > 1:
#     print(result[0][0])
# else:
# if len(antena) % 2 == 0:
#     mid = antena[len(antena) // 2 - 1]
# else:
#     mid = antena[len(antena) // 2]
#
# print(mid)

import sys

n = int(sys.stdin.readline())
antena = list(map(int, sys.stdin.readline().split()))

antena.sort()

if len(antena) % 2 == 0:
    mid = antena[len(antena) // 2 - 1]
else:
    mid = antena[len(antena) // 2]

print(mid)