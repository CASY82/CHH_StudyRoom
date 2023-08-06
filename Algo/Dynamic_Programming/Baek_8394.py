import sys

n = int(sys.stdin.readline())

a1 = 1
a2 = 2
result = 0

if n == 1:
    print(1)
elif n == 2:
    print(2)
else:
    for i in range(3, n+1):
        result = (a2 + a1) % 10
        a1 = a2
        a2 = result

    print(result)

# 다른 사람 풀이

# import sys
#
#
# def a(n):
#     if n > 1:
#         i = 2
#         a, b = 0, 1
#         for i in range(2, n + 1):
#             a, b = b, a + b
#             if b >= 10:
#                 b -= 10
#         return b
#     elif n == 1:
#         return 1
#
#
# print(a(int(sys.stdin.readline()) + 1))