# import sys
#
# case = int(sys.stdin.readline())
#
# for i in range(1, case + 1):
#     n = int(sys.stdin.readline())
#     res = 0
#
#     if n % 2 == 0:
#         tmp = str(bin(n - 1)).count("1")
#         res = tmp + 1
#     else:
#         if n > 2:
#             tmp = str(bin(n - 2)).count("1")
#             res = tmp + 1
#         else:
#             res = 1
#
#     print("Case #{0}: {1}".format(i, res))

import sys

def trailing_ones(n: int) -> int:
    t = 0
    while n & 1:
        t += 1
        n >>= 1
    return t

def popcount(n: int) -> int:
    # 모든 파이썬 버전에서 동작
    return bin(n).count('1')
    # 또는 더 빠른 방법:
    # c = 0
    # while n:
    #     n &= n - 1
    #     c += 1
    # return c

def solve_case(n: int) -> int:
    L = n.bit_length()
    if n == (1 << L) - 1:     # 모두 1인 형태(1,3,7,15,...)면 L
        return L
    t = trailing_ones(n)      # 뒤쪽 연속된 1의 개수
    return popcount(n) + (L - 1 - t)


t = int(sys.stdin.readline().strip())

for i in range(1, t + 1):
    n = int(sys.stdin.readline())
    ans = solve_case(n)
    print(f"Case #{i}: {ans}")