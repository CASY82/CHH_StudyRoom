import sys

t = int(sys.stdin.readline())

cost = [350.34, 230.90, 190.55, 125.30, 180.90]

for _ in range(t):
    cnt = list(map(int, sys.stdin.readline().split()))
    result = 0

    for i in range(5):
        result += cnt[i] * cost[i]

    print("${0:.2f}".format(result))