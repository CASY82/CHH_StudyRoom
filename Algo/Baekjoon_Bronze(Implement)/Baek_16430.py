import sys

a, b = map(int, sys.stdin.readline().split())

p = b - a
q = b

for i in range(1, 9):
    if p % i == 0 and q % i == 0:
        p //= i
        q //= i

print(p, q)