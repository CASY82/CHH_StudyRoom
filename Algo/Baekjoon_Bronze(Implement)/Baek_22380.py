import sys

while True:
    n, m = map(int, sys.stdin.readline().split())

    if n == m == 0:
        break

    need_money = m // n
    result = 0

    friends_money = list(map(int, sys.stdin.readline().split()))

    for money in friends_money:
        if money - need_money < 0:
            result += money
        else:
            result += need_money

    print(result)