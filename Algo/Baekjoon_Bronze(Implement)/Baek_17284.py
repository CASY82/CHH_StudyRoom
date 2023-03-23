import sys

button = list(map(int, sys.stdin.readline().split()))

price = [500, 800, 1000]
money = 5000

for btn in button:
    money -= price[btn-1]

print(money)