# Большой удой

import sys

l = int(sys.stdin.readline())
t = int(sys.stdin.readline())

big = max((l - t), t)
small = min((l - t), t)

print(big - small)