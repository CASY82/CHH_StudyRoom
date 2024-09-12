import sys

n = int(sys.stdin.readline())
candy = list(map(int, sys.stdin.readline().split()))

candy.sort()
total = sum(candy)
index = 0

while total % 2 == 1:
    if candy[index] % 2 == 1:
        total -= candy[index]
    index += 1

print(total)

# 다른 사람 풀이
# import sys
#
# input = sys.stdin.readline
#
# def solution():
#     input()
#     A = tuple(map(int, input().split()))
#     res = cnt = 0
#     odd_numbers = []
#     for a in A:
#         if a%2 == 0:
#             res += a
#         else:
#             odd_numbers.append(a)
#             cnt += 1
#     res += sum(odd_numbers)
#     if cnt%2:
#         res -= min(odd_numbers)
#     print(res)
#
# solution()