import sys

a = int(sys.stdin.readline())
x = int(sys.stdin.readline())
b = int(sys.stdin.readline())
y = int(sys.stdin.readline())
t = int(sys.stdin.readline())

a_tmp = (t - 30) * x * 21
b_tmp = (t - 45) * y * 21

if a_tmp < 0:
    a_tmp = 0

if b_tmp < 0:
    b_tmp = 0

a_result = a + a_tmp
b_result = b + b_tmp

print(a_result, b_result)