import sys
from bisect import bisect_left

n = int(sys.stdin.readline())
num = list(map(int, sys.stdin.readline().split()))

newNum = [-1000000001]
result = []

for i in num:
    if newNum[-1] < i:
        newNum.append(i)
        result.append((i, len(newNum)-1))
    else:
        idx = bisect_left(newNum, i)
        newNum[idx] = i
        result.append((i, idx))

comp = len(newNum)-1
arr = []

for i in range(n-1, -1, -1):
    if result[i][1] == comp:
        arr.append(result[i][0])
        comp -= 1

arr.reverse()

print(len(newNum)-1)
for i in arr:
    print(i, end=" ")