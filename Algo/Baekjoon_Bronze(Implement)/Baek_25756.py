# 포맷 맞추려고 별짓을 다했는데 이렇게 할 필요 없었다...
# import sys
# from decimal import Decimal, getcontext
#
# getcontext().prec = 8
#
# n = int(sys.stdin.readline())
# block_ignore = list(map(int, sys.stdin.readline().split()))
#
# v = 0
#
# def format_decimal(num):
#     str_num = str(num)
#     if '.' in str_num:
#         str_num = str_num.rstrip('0').rstrip('.')
#     return str_num
#
# for i in range(n):
#     v = (1 - (1 - v) * (1 - Decimal(block_ignore[i] / 100)))
#     tmp = v * 100
#
#     print(format_decimal(tmp))

import sys

n = int(sys.stdin.readline())
block_ignore = list(map(int, sys.stdin.readline().split()))

v = 0
for i in range(n):
    v = (1 - (1 - v) * (1 - (block_ignore[i] / 100)))
    print(v * 100)