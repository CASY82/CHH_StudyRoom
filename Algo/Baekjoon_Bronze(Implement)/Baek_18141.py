import sys

n = int(sys.stdin.readline())
num = list(map(int, sys.stdin.readline().split()))
check = False

for i in range(n):
    for j in range(n):
        for k in range(n):
            if i != j != k:
                if int((num[i] - num[j]) / num[k]) != (num[i] - num[j]) // num[k]:
                    check = True
                    break

        if check:
            break
    if check:
        break

if check:
    print("no")
else:
    print("yes")

# 다른 사람 풀이
# import sys
#
# input = sys.stdin.readline
#
# n = int(input())
# numbers = list(map(int, input().split()))
#
#
# def solution():
#     for i in range(n):
#         for j in range(n):
#             for k in range(n):
#                 if i == j or j == k or k == i: continue
#
#                 ftmp = (numbers[i] - numbers[j]) % numbers[k]
#                 if ftmp > 0:
#                     print('no')
#                     return
#
#     print('yes')
#
#
# solution()