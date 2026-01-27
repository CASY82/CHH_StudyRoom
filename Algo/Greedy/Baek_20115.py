# 에너지 드링크
import sys

n = int(sys.stdin.readline())
drinks = list(map(int, sys.stdin.readline().split()))

large = max(drinks)
sum_drink = sum(drinks)

print(large + (sum_drink - large) / 2)