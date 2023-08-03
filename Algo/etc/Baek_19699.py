import sys
import math
import itertools

def get_all_combinations(cows, pick):
    return list(itertools.combinations(cows, pick))

max_weight = 10000

array = [True for i in range(max_weight + 1)]
prime = set()

for i in range(2, int(math.sqrt(max_weight)) + 1):
    if array[i]:
        j = 2
        while i * j <= max_weight:
            array[i * j] = False
            j += 1

for i in range(2, max_weight + 1):
    if array[i]:
        prime.add(i)

n, m = map(int, sys.stdin.readline().split())
cow_weights = list(map(int, sys.stdin.readline().split()))

result = []

for select in get_all_combinations(cow_weights, m):
    tmp = sum(select)
    if tmp in prime and tmp not in result:
        result.append(tmp)

result.sort()

if len(result) > 0:
    for res in result:
        print(res, end=" ")
else:
    print(-1)