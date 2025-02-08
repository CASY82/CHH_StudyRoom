# import sys
#
# a, b = map(int, sys.stdin.readline().split())
# c, d = map(int, sys.stdin.readline().split())
# total = 0
#
# if c <= a < d:
#     total += abs(b - a) + abs(a - c)
# elif c <= b < d:
#     total += abs(b - a) + abs(d - b)
# elif a <= c and d <= b:
#     total += abs(b - a)
# else:
#     total += abs(b - a) + abs(d - c)
#
# print(total)

import sys

# 입력 받기
a, b = map(int, sys.stdin.readline().split())
c, d = map(int, sys.stdin.readline().split())

# 두 구간의 길이를 계산하기
start = max(a, c)  # 두 구간의 시작점
end = min(b, d)    # 두 구간의 끝점

# 두 구간의 길이 계산
if start < end:
    # 겹치는 부분이 있을 경우
    total_length = (b - a) + (d - c) - (end - start)
else:
    # 겹치는 부분이 없을 경우
    total_length = (b - a) + (d - c)

# 결과 출력
print(total_length)