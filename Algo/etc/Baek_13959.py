# import sys
#
# d = int(sys.stdin.readline())
# r = int(sys.stdin.readline())
# t = int(sys.stdin.readline())
#
# def sum_age(n, start):
#     return (n * (n + 1) // 2) - (start * (start + 1) // 2)
#
# tmp = 0
#
# for i in range(4, 50):
#     if sum_age(i, 4) + sum_age(i - d, 3) == r + t:
#        tmp = i
#
# print(tmp)

import sys

D = int(sys.stdin.readline())
R = int(sys.stdin.readline())  # 리타 상자 현재 개수
T = int(sys.stdin.readline())  # 테오 상자 현재 개수

def sum_range(a, n):
    """정수 a..n의 합 (n<a면 0)"""
    if n < a:
        return 0
    cnt = n - a + 1
    return (a + n) * cnt // 2

S = R + T  # 두 상자 총합

# 리타 나이 r는 최소 4, 테오 나이 r-D는 최소 3
for r_now in range(max(4, D + 3), 120):  # 상한은 넉넉히
    t_now = r_now - D
    SR = sum_range(4, r_now)   # 리타: 4..r_now
    ST = sum_range(3, t_now)   # 테오: 3..t_now
    if SR + ST == S:
        print(R - SR)          # 리타가 꺼내야 하는 개수
        break