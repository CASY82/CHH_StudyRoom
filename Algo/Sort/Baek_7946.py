import sys

t = int(sys.stdin.readline())

for _ in range(t):
    n, k = map(int, sys.stdin.readline().split())
    money = list(map(int, sys.stdin.readline().split()))

    money.sort()

    print(money[k-1])