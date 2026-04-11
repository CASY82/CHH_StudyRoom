# Космические захватчики

import sys

n, p = map(int, sys.stdin.readline().split())
monsters = list(map(int, sys.stdin.readline().split()))

# 외계인은 어떤 구간이든 최소 1 이상
short = min(abs(n - p), abs(p - 1))
long = max(abs(n - p), abs(p - 1))

print(short * 2 + sum(monsters) + long)