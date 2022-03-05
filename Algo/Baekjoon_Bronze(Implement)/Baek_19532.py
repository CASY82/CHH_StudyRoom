import sys

a, b, c, d, e, f = map(int, sys.stdin.readline().split())

x = (e*c + (-b)*f) // ((a * e) - (b * d))
y = ((-d)*c + a * f) // ((a * e) - (b * d))

print(x, y)