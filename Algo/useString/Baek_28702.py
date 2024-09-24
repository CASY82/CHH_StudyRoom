import sys

s = sys.stdin.readline().strip()
t = sys.stdin.readline().strip()

s_len = len(s)
t_len = len(t)

new_s = [s for _ in range(t_len)]
new_t = [t for _ in range(s_len)]

if "".join(new_t) == "".join(new_s):
    print(1)
else:
    print(0)

# 다른 사람 풀이
# import math
#
# def lcm(a, b) :
#     return abs(a * b) // math.gcd(a, b)
#
# s = input()
# f = input()
#
# a = lcm(len(s), len(f))
#
# S = s * (a//len(s))
# F = f * (a//len(f))
#
# if S == F :
#     print(1)
# else :
#     print(0)