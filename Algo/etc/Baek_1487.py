import sys

n = int(sys.stdin.readline())
buyer = []

for _ in range(n):
    cell, beadalfee = map(int, sys.stdin.readline().split())

    buyer.append([cell, beadalfee, 0])

for i in range(n):
    tmp = buyer[i][0]
    for j in range(n):
        if buyer[i][0] <= buyer[j][0]:
            buyer[i][2] += max(0, tmp - buyer[j][1])

buyer.sort(key=lambda x : (-x[2], x[0]))
check = True

for i in range(n):
    if buyer[i][2] > 0:
        check = False
        print(buyer[i][0])
        break

if check:
    print(0)

# 다른 사람 풀이
# n = int(input())
# userMoney_deliMoney = []
#
# for _ in range(n):
#     temp = list(map(int, input().split()))
#     userMoney_deliMoney.append(temp)
#
# result = []
#
# for i in range(n):
#     sejunMoney = userMoney_deliMoney[i][0]
#     temp = 0
#     for user in range(n):
#         if sejunMoney <= userMoney_deliMoney[user][0] and sejunMoney > userMoney_deliMoney[user][1]:
#             temp += sejunMoney - userMoney_deliMoney[user][1]
#     result.append((temp, sejunMoney))
#
# # 이익이 최대인 값을 찾기
# max_profit = max(result, key=lambda x: x[0])[0]
#
# # 최대 이익을 가진 가격들 중 가장 낮은 가격을 선택
# max_prices = [price for profit, price in result if profit == max_profit]
#
# if max_profit != 0:
#     print(min(max_prices))
# else:
#     print(0)
