import sys

n, m = map(int, sys.stdin.readline().split())

price = []

for _ in range(m):
    price.append(int(sys.stdin.readline()))

price.sort(reverse=True)
result_price = 0
result_revenue = 0

for i in range(m):
    if n > i:
        tmp = price[i] * (i+1)
        if result_revenue < tmp:
            result_revenue = tmp
            result_price = price[i]
    else:
        break

print(result_price, result_revenue)