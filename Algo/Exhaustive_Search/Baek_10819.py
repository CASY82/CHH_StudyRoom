import sys
from itertools import permutations

n = int(sys.stdin.readline())

num = list(map(int, sys.stdin.readline().split()))
result = 0

for numList in list(permutations(num)):
    sum_num = 0
    for j in range(len(numList)-1):
        sum_num += abs(numList[j] - numList[j + 1])

    if result < sum_num:
        result = sum_num

print(result)