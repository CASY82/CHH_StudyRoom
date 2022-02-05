# import sys
#
# n = int(sys.stdin.readline())
# num = list(map(int, sys.stdin.readline().split()))
#
# start = min(num)
# end = max(num)
# numList = set()
# length = 6
#
# while start <= end:
#     mid = (start + end) // 2
#     cnt = 0
#
#     for i in num:
#         if mid < i:
#             if i not in numList:
#                 numList.add(i)
#                 cnt += 1
#
#     if cnt < length:
#         start = mid + 1
#     else:
#         end = mid - 1
#         length = cnt
#
# print(length)

# LIS문제를 푸는 방법을 찾아보아서 풀긴했다... 새로운 방법을 알게 되었다!
import sys

n = int(sys.stdin.readline())
num = list(map(int, sys.stdin.readline().split()))

memorize = [0]

for case in num:
    if memorize[-1] < case:
        memorize.append(case)
    else:
        start = 0
        end = len(memorize)

        while start < end:
            mid = (start + end) // 2

            if memorize[mid] < case:
                start = mid + 1
            else:
                end = mid

        memorize[end] = case

print(len(memorize)-1)