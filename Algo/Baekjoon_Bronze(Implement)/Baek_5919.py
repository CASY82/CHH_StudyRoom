import sys

n = int(sys.stdin.readline())
mow = []
tmp = 0
res = 0

for _ in range(n):
    hay = int(sys.stdin.readline())

    mow.append(hay)
    tmp += hay

tmp //= n

for haytmp in mow:
    res += abs(haytmp - tmp)

print(res // 2)