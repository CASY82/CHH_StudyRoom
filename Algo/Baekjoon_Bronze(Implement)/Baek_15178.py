import sys

n = int(sys.stdin.readline())

for _ in range(n):
    num = list(map(int, sys.stdin.readline().split()))

    if sum(num) == 180:
        print(*num, "Seems OK")
    else:
        print(*num, "Check")