import sys

a, b = map(int, sys.stdin.readline().split())

a_100 = 100 - a
b_100 = 100 - b

d = (a_100 * b_100)
c = 100 - (a_100 + b_100)

q = d // 100
r = d % 100

print(a_100, b_100, c, d, q, r)
print(c + q, r)