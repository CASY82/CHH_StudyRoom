import sys

n = int(sys.stdin.readline())
price = []

for _ in range(n):
    price.append(float(sys.stdin.readline()))

price.sort()
print("{:.2f}".format(price[1]))