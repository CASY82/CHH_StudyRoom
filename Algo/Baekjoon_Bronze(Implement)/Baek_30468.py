import sys

s, d, i, l, n = map(int, sys.stdin.readline().split())

total = (s + d + i + l)
tmp = n * 4

bless = 0

while True:
    if total >= tmp:
        break

    total += 1
    bless += 1

print(bless)