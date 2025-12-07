import sys
import math

a, b = map(int, sys.stdin.readline().split())
g = math.gcd(a, b)

# 한 번에 만들기 (g <= 10^7 이므로 메모리 괜찮음)
sys.stdout.write('1' * g)