import sys

n = int(sys.stdin.readline())
num = list(map(int, sys.stdin.readline().split()))

newNumList = [0 for _ in range(n)]

for i in range(len(newNumList)):
    newNumList[i] = num[i]
    for j in range(i):
        if num[i] > num[j]:
            newNumList[i] = max(newNumList[i], newNumList[j] + num[i])

print(max(newNumList))