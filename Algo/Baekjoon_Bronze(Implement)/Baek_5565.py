import sys

total = int(sys.stdin.readline())
price = []

for i in range(9):
    price.append(int(sys.stdin.readline()))

print(total - sum(price))