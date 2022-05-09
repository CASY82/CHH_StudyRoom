import sys

n, w = map(int, sys.stdin.readline().split())

coin = []

for _ in range(n):
    coin.append(int(sys.stdin.readline()))

now_money = w
now_coin = 0
buy = True

for i in range(len(coin)):
    if len(coin) - 1 > i:
        if buy:
            if coin[i] < coin[i + 1]:
                now_coin = now_money // coin[i]
                now_money = now_money % coin[i]
                buy = False
            else:
                continue
        else:
            if coin[i] > coin[i + 1]:
                now_money += now_coin * coin[i]
                now_coin = 0
                buy = True
            else:
                continue
    else:
        if buy:
            break
        else:
            now_money += now_coin * coin[i]
            now_coin = 0

print(now_money)