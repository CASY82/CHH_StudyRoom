import sys
from itertools import combinations

n = int(sys.stdin.readline())
compareList = []

for i in range(n):
    num = list(map(int, sys.stdin.readline().split()))
    maxMon = 0

    resultComb = list(map(list, combinations(num, 3)))

    for i in range(len(resultComb)):
        tmp = sum(resultComb[i])
        tmp %= 10
        if tmp > maxMon:
            maxMon = tmp

    compareList.append(maxMon)

people = 0
for i in range(n):
    if max(compareList) == compareList[i]:
        people = i

print(people+1)