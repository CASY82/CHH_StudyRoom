# Patterns and Pictures

import sys

n = int(sys.stdin.readline())
yard_set = 36 * 36

for _ in range(n):
    i = int(sys.stdin.readline())
    tmp = 0

    for _ in range(i):
        s, r = map(int, sys.stdin.readline().split())

        tmp += s * r

    print(yard_set // tmp, yard_set * 2 // tmp, yard_set * 3 // tmp)