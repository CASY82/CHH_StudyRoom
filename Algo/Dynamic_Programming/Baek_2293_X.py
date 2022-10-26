import sys

n, k = map(int, sys.stdin.readline().split())
coin = []
check = [0 for _ in range(k+1)]

check[0] = 1

for _ in range(n):
    value = int(sys.stdin.readline())
    coin.append(value)

for i in range(n):
    for j in range(coin[i], k+1):
        check[j] += check[j-coin[i]]

print(check[k])