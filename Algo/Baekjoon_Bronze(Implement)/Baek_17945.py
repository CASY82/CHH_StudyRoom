import sys
import math

a = 1
b, c = map(int, sys.stdin.readline().split())

plus = -b + math.sqrt(b * b - a * c) // a
minus = -b - math.sqrt(b * b - a * c) // a

tmp = [int(plus), int(minus)]
tmp.sort()

if tmp[0] == tmp[1]:
    print(tmp[0])
else:
    print(*tmp)