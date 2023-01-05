# 에이씨... 이거 메모리 오버함...
# import sys
# sys.setrecursionlimit(300000)
#
# n = int(sys.stdin.readline())
# num = list(map(int, sys.stdin.readline().split()))
#
# def half(num_list, depth):
#     if len(num_list) == 2 * depth:
#         num_list.sort()
#         return num_list
#     else:
#         return half(num_list[:n//2], depth) + half(num_list[n//2:], depth)
#
# k = int(sys.stdin.readline())
# print(*half(num, k))

#매우 간단한 코드가 있었네?
import sys

n = int(sys.stdin.readline())
num = list(map(int, sys.stdin.readline().split()))

k = int(sys.stdin.readline())

tmp = n // k

for i in range(0, n, tmp):
    num_list = num[i:i+tmp]
    num_list.sort()

    print(*num_list, end=" ")