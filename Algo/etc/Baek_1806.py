# 처음 시도한 코드.. 답도 잘안나오네...
# import sys
#
# n, s = map(int, sys.stdin.readline().split())
# num = list(map(int, sys.stdin.readline().split()))
#
# start = 0
# end = 1
# length = 100001
# check = False
#
# while True:
#     if end == len(num) and start == end - 1:
#         break
#
#     if sum(num[start:end]) >= s:
#         check = True
#         if end - start < length:
#             length = end - start + 1
#         start += 1
#
#     else:
#         if end != len(num)-1:
#             end += 1
#         else:
#             start += 1
#
#     if end == start:
#         end += 1
#
# if check:
#     print(length)
# else:
#     print(0)

#기존에 배웠던 투 포인터 공식을 활용했다. 책을 좀 참고하여 풀긴했는데.. 그래도 성공!
import sys

n, s = map(int, sys.stdin.readline().split())
num = list(map(int, sys.stdin.readline().split()))

start = 0
end = 0
interval_sum = 0
length = 100001
check = False

for start in range(n):
    while interval_sum < s and end < n:
        interval_sum += num[end]
        end += 1

    if interval_sum >= s:
        check = True
        if length > end - start:
            length = end - start
    interval_sum -= num[start]

if check:
    print(length)
else:
    print(0)