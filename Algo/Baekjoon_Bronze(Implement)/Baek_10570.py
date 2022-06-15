import sys

n = int(sys.stdin.readline())

for _ in range(n):
    v = int(sys.stdin.readline())

    num = [0] * 1001
    for i in range(v):
        s = int(sys.stdin.readline())

        num[s] += 1

    print(num.index(max(num)))