import sys
import math

a, b = map(int, sys.stdin.readline().split())

g = math.gcd(a, b)

divs = []
limits = int(g**0.5)

for i in range(1, limits + 1):
    if g % i == 0:
        divs.append(i)
        if i != g // i:
            divs.append(g // i)

for j in sorted(divs):
    print(j, a // j, b // j)