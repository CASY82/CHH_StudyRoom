import sys

a1, a0 = map(int, sys.stdin.readline().split())
c = int(sys.stdin.readline())
n0 = int(sys.stdin.readline())

fn = a1 * n0 + a0
gn = c * n0

if fn <= gn and a1 <= c:
    print(1)
else:
    print(0)