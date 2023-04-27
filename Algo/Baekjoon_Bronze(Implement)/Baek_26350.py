import sys

n = int(sys.stdin.readline())

for _ in range(n):
    numList = list(map(int, sys.stdin.readline().split()))

    coins = numList[1:]
    before = 0
    really = True

    for coin in coins:
        if before == 0:
            before = coin
        else:
            if before * 2 > coin:
                really = False
                break

            before = coin

    print("Denominations:", *coins)
    if really:
        print("Good coin denominations!")
    else:
        print("Bad coin denominations!")
    print()