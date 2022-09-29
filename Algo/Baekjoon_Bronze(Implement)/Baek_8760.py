import sys

t = int(sys.stdin.readline())

for _ in range(t):
    w, k = map(int, sys.stdin.readline().split())

    print((w*k) // 2)