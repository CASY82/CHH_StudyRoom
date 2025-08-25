import sys
from math import gcd
from fractions import Fraction

data = list(map(int, sys.stdin.read().split()))
if len(data) >= 3:
    n, p, q = data[:3]
else:
    n, p, q = map(int, input().split())

fractions = []
for b in range(1, n + 1):       # 분모 b
    for a in range(1, b):       # 분자 a (진분수만)
        if gcd(a, b) != 1:
            continue            # 기약분수만
        # 1/p < a/b < 1/q  (모두 양수이므로 교차곱 사용)
        if a * p > b and a * q < b:
            fractions.append((a, b, Fraction(a, b)))

# 값 기준 오름차순 정렬
fractions.sort(key=lambda x: x[2])

# 출력
for a, b, _ in fractions:
    print(f"{a}/{b}")