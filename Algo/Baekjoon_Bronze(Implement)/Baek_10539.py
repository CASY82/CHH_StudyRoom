import sys

n = int(sys.stdin.readline())
numList = list(map(int, sys.stdin.readline().split()))
result = []

for i in range(1, n+1):
    if result:
        print((numList[i-1] * i) - sum(result[:i]), end=" ")
        result.append((numList[i-1] * i) - sum(result[:i]))
    else:
        result.append((numList[i-1] * i))
        print((numList[i-1] * i), end=" ")