import sys

b, c, d = map(int, sys.stdin.readline().split())
burger = list(map(int, sys.stdin.readline().split()))
side = list(map(int, sys.stdin.readline().split()))
beverage = list(map(int, sys.stdin.readline().split()))

set_menu = min(b, c, d)

burger.sort(reverse=True)
side.sort(reverse=True)
beverage.sort(reverse=True)

total = sum(burger) + sum(side) + sum(beverage)
discount_total = total

for i in range(set_menu):
    discount_total -= int(burger[i] * 0.1) + int(side[i] * 0.1) + int(beverage[i] * 0.1)

print(total)
print(discount_total)