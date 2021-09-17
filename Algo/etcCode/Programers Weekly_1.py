price = 3
money = 20
count = 4

def solution(price, money, count):
    for i in range(1, count + 1):
        money -= (price * i)

    if money > 0:
        return 0
    else:
        return -money

print(solution(price, money, count))

