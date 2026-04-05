# 사람의 수
import sys

input = sys.stdin.readline

n = int(input())
arr = []

for _ in range(n):
    s = input().strip()
    integer, decimal = s.split(".")
    arr.append(int(integer) * 1000 + int(decimal))

for m in range(1, 1002):
    ok = True

    for p in arr:
        l = p * m
        r = (p + 1) * m

        first_multiple = ((l + 999) // 1000) * 1000

        if first_multiple >= r:
            ok = False
            break

    if ok:
        print(m)
        break