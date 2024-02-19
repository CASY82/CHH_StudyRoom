import sys

n = int(sys.stdin.readline())
coins = list(map(int, sys.stdin.readline().split()))

one = coins.count(1)
zero = coins.count(0)

print(min(one, zero))