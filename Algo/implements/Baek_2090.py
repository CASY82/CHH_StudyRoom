import sys
import math
from functools import reduce

n = int(sys.stdin.readline())
num = list(map(int, sys.stdin.readline().split()))

# 두 수의 최소 공배수 계산
def lcm(a, b):
    return abs(a * b) // math.gcd(a, b)

# 여러 수의 최소 공배수 계산
def lcm_multiple(numbers):
    return reduce(lcm, numbers)

def simplify_fraction(numerator, denominator):
    gcd = math.gcd(numerator, denominator)  # 최대공약수 구하기
    simplified_numerator = numerator // gcd  # 약분된 분자
    simplified_denominator = denominator // gcd  # 약분된 분모
    return simplified_numerator, simplified_denominator

my_gcd = lcm_multiple(num)
tmp = 0

for i in range(len(num)):
    tmp += my_gcd // num[i]

res = simplify_fraction(my_gcd, tmp)

print("{0}/{1}".format(res[0], res[1]))

# 유클리드 호제법 사용해도 됨
# 다른 사람 풀이
# from fractions import Fraction
#
# N = int(input())
# L = list(map(int, input().split()))
# temp = 0
# if len(L) != 1:
#     for i in range(N):
#         temp += Fraction(1, L[i])
#     print(1/temp)
# else:
#     print(f"{L[0]}/{1}")