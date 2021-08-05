#거스름돈

money = int(input())
coins = [500, 100, 50, 10]
count = 0

for i in coins:
    if money != 0:
        count += (money // i)
        money -= i * (money // i)

print(count)


#예시 답

# n = 1260
#
# coin_types = [500, 100, 50, 10]
#
# for coin in coin_types:
#     count += n // coin
#     n %= coin
#
# print(count)