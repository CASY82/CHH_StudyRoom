# Matryoshka Dolls
import sys
from collections import Counter

while True:
    n = int(sys.stdin.readline())

    if n == 0:
        break

    tmp = []

    for _ in range(n):
        tmp.append(int(sys.stdin.readline()))

    print(Counter(tmp).most_common(1)[0][1])