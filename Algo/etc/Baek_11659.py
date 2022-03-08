import sys

n, m = map(int, sys.stdin.readline().split())
num = list(map(int, sys.stdin.readline().split()))
sumList = []
sumTmp = 0

for start in range(len(num)):
    sumTmp += num[start]
    sumList.append(sumTmp)

for _ in range(m):
    i, j = map(int, sys.stdin.readline().split())

    if i >= 2:
        result = sumList[j-1] - sumList[i-2]
    else:
        result = sumList[j-1]

    print(result)