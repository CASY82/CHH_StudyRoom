# 백트래킹으로 풀어도됬네...
import sys
from itertools import combinations
from functools import reduce
import operator

n = int(sys.stdin.readline())
ingredients = []
res = 9999999999999999

for _ in range(n):
    sin, ssun = map(int, sys.stdin.readline().split())
    res = min(res, abs(sin - ssun))

    ingredients.append([sin, ssun])

for i in range(1, n + 1):
    for comb in combinations(ingredients, i):
        sin_values = [item[0] for item in comb]
        ssun_values = [item[1] for item in comb]

        sin_product = reduce(operator.mul, sin_values, 1)
        ssun_sum = sum(ssun_values)

        res = min(res, abs(sin_product - ssun_sum))

print(res)