import sys
import math

a = int(sys.stdin.readline())
res = 2 * math.sqrt(a * math.pi)
res = round(res, 6)

print(f"{res:.6f}")