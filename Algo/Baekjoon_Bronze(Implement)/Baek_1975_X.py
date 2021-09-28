# t = int(input())
# data = [0]
#
# for i in range(1, 1001):
#     count = 0
#     for j in range(2, i + 1):
#         if i % j == 0:
#             count += 1
#
#     data.append(count)
#
# print(data)
#
# for _ in range(t):
#     n = int(input())
#
#     print(data[n])
# 문제를 전혀 이해 못하겠음 왜 나눈 수를 또나누고 나누고..?

import sys
input = sys.stdin.readline

def func(x, b):
    if x !=0 and x % b == 0: return 1+func(x//b,b)
    else: return 0

c = [0] * 1001
for x in range(2, 1001):
    c[x] = sum(func(x, b) for b in range(2, x+1))

print(c)

for _ in range(int(input())):
    x = int(input())
    print(c[x])