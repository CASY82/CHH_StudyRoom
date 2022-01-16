import sys
from collections import Counter

n = int(sys.stdin.readline())
card = []

for _ in range(n):
    card.append(int(sys.stdin.readline()))

card.sort()
count = Counter(card)
result = list(count.most_common()[0])
print(result[0])