import sys

changer = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "A", "B", "C", "D", "E", "F"]

m, n = map(int, sys.stdin.readline().split())

res = ""

while True:
    res += changer[m % n]

    m //= n

    if m == 0:
        break

print(res[::-1])

# 다른 사람 풀이
# def trans(a, b):
#     global t
#     if a < b:
#         return str(t[a])
#     else:
#         return trans(a // b, b) + str(t[a % b])
#
#
# m, n = map(int, input().split())
#
# t = '0123456789ABCDEF'
#
# print(trans(m, n))