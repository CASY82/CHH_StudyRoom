import sys

n = int(sys.stdin.readline())
a, b = map(int, sys.stdin.readline().split())

zero = a + b - n
binary = ""

if zero <= 0:
    for i in range(n):
        if a + b > i:
            binary += "1"
        else:
            binary += "0"
else:
    binary += (n - zero) * "1"
    binary += zero * "0"

print(int(binary.replace(' ', ''), 2))

# 다른 사람 풀이
# n = int(input())
# a, b = map(int, input().split())
# if n < a + b:
#     m = 2 * n - a - b
# else:
#     m = a + b
# print(((1 << m) - 1) << (n - m))