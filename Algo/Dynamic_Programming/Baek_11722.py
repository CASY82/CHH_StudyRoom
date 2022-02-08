import sys

n = int(sys.stdin.readline())
num = list(map(int, sys.stdin.readline().split()))

newNumList = [0 for _ in range(n)]

for i in range(n):
    newNumList[i] = 1
    for j in range(n):
        if num[i] < num[j]:
            newNumList[i] = max(newNumList[i], newNumList[j] + 1)

print(max(newNumList))