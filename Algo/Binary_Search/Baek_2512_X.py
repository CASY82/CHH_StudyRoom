# 반례가 발생
# 2
# 10 1
# 5

# 10
# 1 1 1 1 11 11 11 11 11 100
# 100

# import sys
#
# n = int(sys.stdin.readline())
# budget = list(map(int, sys.stdin.readline().split()))
# m = int(sys.stdin.readline())
#
# # 1. 지방의 개수로 최대 예산 나누기
# tmp = m // n
#
# # 2. 남는 예산과 예산이 부족한 도시 개수 구하기
# if sum(budget) <= m:
#     result = max(budget)
# else:
#     reminder = 0
#     cnt = 0
#     for i in range(n):
#         if budget[i] < tmp:
#             reminder += tmp - budget[i]
#         else:
#             cnt += 1
#
#     result = tmp + (reminder // cnt)
#
# print(result)

import sys

n = int(sys.stdin.readline())
budget = list(map(int, sys.stdin.readline().split()))
m = int(sys.stdin.readline())

start = 0
end = max(budget)

if sum(budget) <= m:
    print(end)
else:
    while start <= end:
        total = 0
        mid = (start + end) // 2

        for i in budget:
            #예산과 mid중 작은걸 더해준다는 생각을 못했음...
            total += min(mid, i)

        if total > m:
            end = mid - 1
        else:
            start = mid + 1

    #end, mid뭘찍어야 하는지 헷갈렸다.
    print(end)
