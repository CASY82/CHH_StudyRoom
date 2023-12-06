import sys

n, m = map(int, sys.stdin.readline().split())

brand = list(map(int, sys.stdin.readline().split()))
max_brand = 0

for i in range(1, m + 1):
    tmp = brand.count(i)
    if max_brand < tmp:
        max_brand = tmp

print(max_brand)