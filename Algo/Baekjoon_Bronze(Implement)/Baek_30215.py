import sys

o, a, k = map(int, sys.stdin.readline().split())
res = 0

for i in range(1, o + 1):
    for j in range(1, o + 1):
        if o == a * i + k * j:
            res = 1
            break
    if res == 1:
        break

print(res)