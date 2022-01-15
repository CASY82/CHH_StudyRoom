import sys

n, c = map(int, sys.stdin.readline().split())
num = list(map(int, sys.stdin.readline().split()))
numSet = list(set(num))
countNum = []

for i in numSet:
    countNum.append([i, num.count(i), num.index(i)])

countNum.sort(key=lambda x:(-x[1], x[2]))

for i in range(len(countNum)):
    for j in range(countNum[i][1]):
        print(countNum[i][0], end=' ')