# def bitonic(arr):
#     length = len(arr)
#     tmp = 0
#     while (tmp + 1) < length and arr[tmp] < arr[tmp + 1]:
#         tmp += 1
#     if tmp == 0 or tmp == length - 1:
#         print("NO")
#         return
#     while (tmp + 1) < length and arr[tmp] > arr[tmp + 1]:
#         tmp += 1
#     if tmp != length - 1:
#         print("NO")
#         return
#
#     print("YES")
#     print(tmp)

# 역순으로 진행하는 방법을 좀 다르게 했어야 됬다 이부분은 힌트를 받아서 했으므로 X
import sys

n = int(sys.stdin.readline())
num = list(map(int, sys.stdin.readline().split()))
reNum = num.copy()
reNum.reverse()

cntUpNum = [0 for _ in range(n)]
cntDownNum = [0 for _ in range(n)]
result = [0 for _ in range(n)]

for i in range(n):
    cntUpNum[i] = 1
    cntDownNum[i] = 1
    for j in range(i):
        # 증가하는 것만 체크
        if num[i] > num[j]:
            cntUpNum[i] = max(cntUpNum[i], cntUpNum[j] + 1)
        # 감소하는 것만 체크
        if reNum[i] > reNum[j]:
            cntDownNum[i] = max(cntDownNum[i], cntDownNum[j] + 1)

cntDownNum.reverse()

for i in range(n):
    result[i] = cntUpNum[i] + cntDownNum[i]

print(max(result) - 1)