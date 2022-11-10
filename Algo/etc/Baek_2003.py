import sys
n, m = map(int, sys.stdin.readline().split())
num = list(map(int, sys.stdin.readline().split()))
point1 = 0
point2 = 1
cnt = 0

#재채점으로 인해서 틀림 그래서 다시 품
while point1 <= n-1:
    if sum(num[point1:point2]) == m:
        cnt += 1

    if sum(num[point1:point2]) > m:
        point1 += 1
    else:
        if point2 < n:
            point2 += 1
        else:
            point1 += 1

print(cnt)

#시간이 더 적게 걸린 코드 참고
# n,m = map(int,input().split())
# a = 0
# b = 0
# c = 0
#
# arr = list(input().split())
# for j in range(n):
#     for t in range(j,n):
#         a += int(arr[t])
#         if a == m:
#             b += 1
#             a = 0
#             break
#         elif a > m:
#             a = 0
#             break
#         elif t == n-1 and a < m:
#             a = 0
#             c = 1
#             break
#     if c == 1:
#         break
#
# print(b)

#투 포인터 정석 코드 발견...
# import sys
#
# input = sys.stdin.readline
#
#
# def solution2():
#     n, target = list(map(int, input().split()))
#     numbers = list(map(int, input().split()))
#     start = 0
#     end = 0
#     sum = 0
#     cnt = 0
#     while start < n:
#
#         if sum == target:
#             cnt += 1
#             sum -= numbers[start]
#             start += 1
#
#         elif sum < target:
#             if end == n:
#
#                 break
#             else:
#                 sum += numbers[end]
#                 end += 1
#
#         else:
#             sum -= numbers[start]
#             start += 1
#     print(cnt)
#
#
# solution2()