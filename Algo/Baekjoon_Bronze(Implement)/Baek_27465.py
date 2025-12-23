import sys

n = int(sys.stdin.readline().strip())

if n <= 4:
    print(4)
elif n <= 500_000_000:
    print(2 * n)
else:
    print(1_000_000_000)