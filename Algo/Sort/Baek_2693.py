import sys

t = int(sys.stdin.readline())

for _ in range(t):
    num = list(map(int, sys.stdin.readline().split()))

    num.sort()

    print(num[-3])