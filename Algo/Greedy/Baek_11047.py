import sys

n, k = map(int, sys.stdin.readline().split())

coin = []
cnt = 0

for _ in range(n):
    coin.append(int(sys.stdin.readline()))

for i in range(len(coin)-1, -1, -1):
    if k // coin[i] != 0:
        cnt += k // coin[i]
        k %= coin[i]

    if k <= 0:
        break

print(cnt)