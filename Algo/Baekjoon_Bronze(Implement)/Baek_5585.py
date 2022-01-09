import sys

pay = int(sys.stdin.readline())
money = 1000
cnt = 0
coin = [500, 100, 50, 10, 5, 1]

money -= pay

for i in coin:
    cnt += money // i
    money %= i

    if money <= 0:
        break

print(cnt)