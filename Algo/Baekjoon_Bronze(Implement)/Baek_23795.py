sum_money = 0

while True:
    money = int(input())

    if money < 0:
        break

    sum_money += money

print(sum_money)