import sys

n = int(sys.stdin.readline())

stock = list(map(int, sys.stdin.readline().split()))

max_stock = 0
min_stock = stock[-1]
result = 0

for i in range(n-1, -1, -1):
    if max_stock < stock[i]:
        max_stock = stock[i]
        min_stock = stock[i]

    min_stock = min(min_stock, stock[i])
    result = max(result, max_stock-min_stock)

print(result)

# 다른 사람 풀이
# n = int(input())
# stock = list(map(int, input().split()))
#
# minVal, maxVal = stock[0], 0
# answer = 0
# for i in range(1, n):
#     if minVal < stock[i]:
#         answer = max(answer, stock[i] - minVal)
#     else:
#         minVal = stock[i]
#
# print(answer)