import sys

t = int(sys.stdin.readline())

for _ in range(t):
    s = int(sys.stdin.readline())
    option = int(sys.stdin.readline())

    for _ in range(option):
        q, p = map(int, sys.stdin.readline().split())

        s += q * p

    print(s)