import sys

n = int(sys.stdin.readline())
card = list(map(int, sys.stdin.readline().split()))

card.sort(reverse=True)
total = 0

for i in range(n-1):
    total += card[i] + card[i + 1]
    card[i + 1] = card[i]

print(total)