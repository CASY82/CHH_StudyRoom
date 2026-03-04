# Ромб

import sys

n = int(sys.stdin.readline())
a = int(sys.stdin.readline())
b = int(sys.stdin.readline())

tmp = [[] for _ in range(n)]

for i in range(n):
    for j in range(n):
        if a <= abs(i - (n // 2)) + abs(j - (n // 2)) <= b:
            tmp[i].append("*")
        else:
            tmp[i].append(".")

for k in range(n):
    print("".join(tmp[k]))