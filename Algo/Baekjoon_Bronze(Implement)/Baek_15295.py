# import sys
#
# t = int(sys.stdin.readline())
#
# for _ in range(t):
#     case, day = map(int, sys.stdin.readline().split())
#
#     result = 0
#
#     for i in range(1, day+1):
#         result += i
#
#     print(case, result + day)

import sys

t = int(sys.stdin.readline())

for _ in range(t):
    case, day = map(int, sys.stdin.readline().split())

    result = (day * (day + 1)) // 2

    print(case, result + day)