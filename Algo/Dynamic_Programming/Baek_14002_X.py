# 음... 이전에 이걸로 풀었었는데 틀린다고 나온다. 아무래도 길이만 동일한가보다
# import sys
#
# n = int(sys.stdin.readline())
# num = list(map(int, sys.stdin.readline().split()))
#
# newNum = [0]
#
# for i in range(n):
#     if newNum[-1] < num[i]:
#         newNum.append(num[i])
#     else:
#         for j in range(1, len(newNum)):
#             if newNum[j] >= num[i]:
#                 newNum[j] = num[i]
#                 break
#
# newNum = newNum[1:]
#
# print(len(newNum))
# for i in newNum:
#     print(i, end=" ")
# result 구하는 부분은 도움을 받아서 처리
import sys

n = int(sys.stdin.readline())
num = list(map(int, sys.stdin.readline().split()))

newNum = [0 for _ in range(n)]

for i in range(n):
    newNum[i] = 1
    for j in range(i):
        if num[i] > num[j]:
            newNum[i] = max(newNum[i], newNum[j] + 1)

comp = max(newNum)

result = []

for i in range(n-1, -1, -1):
    if newNum[i] == comp:
        result.append(num[i])
        comp -= 1

result.reverse()

print(max(newNum))
for i in result:
    print(i, end=" ")