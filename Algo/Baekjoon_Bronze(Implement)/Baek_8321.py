import sys

n, k, s = map(int, sys.stdin.readline().split())
box_of_screw = list(map(int, sys.stdin.readline().split()))

box_of_screw.sort(reverse=True)
need_total = k * s
res = 0
tmp = 0

for i in range(n):
    tmp += box_of_screw[i]
    res += 1

    if tmp >= need_total:
        break

print(res)