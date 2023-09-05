# import sys
#
# def round_to_decimal(number, decimal_places):
#     multiplier = 10 ** decimal_places
#     rounded_number = int(number * multiplier + 0.4) / multiplier
#     return int(rounded_number)
#
# while True:
#     B, N = map(int, sys.stdin.readline().split())
#
#     if B == N == 0:
#         break
#
#     tmp = B ** (1 / N)
#
#     print(round_to_decimal(tmp, 0))

# 문제 이해를 잘못함
import sys
input = sys.stdin.readline

while True:
    b, n = map(int, input().split())
    if b == n == 0:
        break
    i = 0
    while i**n < b:
        i += 1

    # 1씩 올리면서 해당 수보다 커지는 시점을 구하면 되는 문제였음;;;
    print(i if i**n-b < b-(i-1)**n else i-1)