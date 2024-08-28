import sys

fir = sys.stdin.readline().strip()
sec = sys.stdin.readline().strip()

union_num = ""

for i in range(8):
    union_num += fir[i] + sec[i]

while len(union_num) != 2:
    tmp = ""

    for i in range(len(union_num) - 1):
        tmp += str((int(union_num[i]) + int(union_num[i + 1])) % 10)

    union_num = tmp

print(union_num)

# 다른 사람 풀이
# import sys, math
# input = sys.stdin.readline
#
# l1 = list(map(int, input().strip()))
# l2 = list(map(int, input().strip()))
# L = []
# for i in range(8):
#     L.append(l1[i])
#     L.append(l2[i])
#
# for i in range(15, 1, -1):
#     LN = []
#     for j in range(i):
#         LN.append((L[j]+L[j+1])%10)
#     L = LN
# print(L[0], L[1], sep='')
