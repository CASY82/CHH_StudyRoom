import sys

b = int(sys.stdin.readline())

p = 5 * b - 400
print(p)
if p > 100:
    print(-1)
elif p == 100:
    print(0)
else:
    print(1)