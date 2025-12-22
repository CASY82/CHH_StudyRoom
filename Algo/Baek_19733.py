import sys
import math

s = sys.stdin.readline().rstrip()
m = s.count('A')

# t(t+1)/2 <= m 를 만족하는 최대 t
t = (math.isqrt(8*m + 1) - 1) // 2
print(t)