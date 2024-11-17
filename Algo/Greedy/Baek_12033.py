import sys

t = int(sys.stdin.readline())

for case in range(t):
    n = int(sys.stdin.readline())
    cost = list(map(int, sys.stdin.readline().split()))

    cost.reverse()
    res = []
    i = 0

    while i < n:
        current = cost[0]
        discount = int(current * 0.75)
        res.append(discount)

        if discount in cost:
            cost.remove(discount)
        cost.remove(current)

        i += 1

    res.sort()
    print("Case #{0}:".format(case + 1), *res)

# 다른 사람 풀이
# from collections import defaultdict
#
# t = int(input())
# for i in range(t):
#     n = int(input())
#     ans = []
#     price = list(map(int, input().split()))
#     price_n = defaultdict(int)
#     for j in price: price_n[j] += 1
#     for j in price:
#         if (not j%3) and price_n[j] and price_n[j*4//3]:
#             ans.append(j)
#             price_n[j] -= 1
#             price_n[j*4//3] -= 1
#     print(f"Case #{i+1}:", " ".join(map(str, ans)))