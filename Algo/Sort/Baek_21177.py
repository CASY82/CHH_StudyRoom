import sys

n = int(sys.stdin.readline())
cards = list(map(int, sys.stdin.readline().split()))

cards.sort()
res = cards[0]

for i in range(1, n):
    if cards[i] - cards[i - 1] > 1:
        res += cards[i]
    else:
        continue

print(res)