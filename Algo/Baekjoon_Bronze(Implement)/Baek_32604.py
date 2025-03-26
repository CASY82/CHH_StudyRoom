import sys

n = int(sys.stdin.readline())
res = True

before_a, before_b = map(int, sys.stdin.readline().split())

for _ in range(n - 1):
    a, b = map(int, sys.stdin.readline().split())

    if before_a > a or before_b > b:
        res = False

    before_a = a
    before_b = b

if res:
    print("yes")
else:
    print("no")