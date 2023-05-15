import sys

n, m = map(int, sys.stdin.readline().split())

nope = [[] for _ in range(n+1)]
result = set()

for _ in range(m):
    suck1, suck2 = list(map(int, sys.stdin.readline().split()))

    nope[suck1].append(suck2)
    nope[suck2].append(suck1)

for i in range(1, n+1):
    for j in range(i+1, n+1):
        for k in range(j+1, n+1):
            if j not in nope[i] and k not in nope[i] and k not in nope[j]:
                result.add((i, j, k))

print(len(result))

# 다른사람 풀이
# n, m = map(int, input().split())
# ice = [[False for _ in range(n)] for _ in range(n)]
# for i in range(m):
#     i1, i2 = map(int, input().split())
#     ice[i1 - 1][i2 - 1] = True
#     ice[i2 - 1][i1 - 1] = True
#
# result = 0
#
# for i in range(n):
#     for j in range(i + 1, n):
#         for k in range(j + 1, n):
#             if not ice[i][j] and not ice[i][k] and not ice[j][k]:
#                 result += 1
#
# print(result)

# 다른사람 풀이 2

# import sys
# input = sys.stdin.readline
# N, M = map(int, input().split())
#
# noMix = {icecreamNum: [] for icecreamNum in range(N+1)}
#
# for _ in range(M):
#     a, b = map(int, input().split())
#     noMix[a].append(b)
#     noMix[b].append(a)
#
#
# for (num, blackList) in noMix.items():
#     if num == 0:
#         continue
#     entireList = [i for i in range(1, N+1)]
#     possibleSetList = list(
#         filter(lambda x: x not in blackList and x > num, entireList))
#     noMix[num] = possibleSetList
#
# possibleList = []
# answer = 0
# for (firstNum, possible) in noMix.items():
#     if firstNum == 0:
#         continue
#     for secondNum in noMix[firstNum]:
#         for thirdNum in noMix[secondNum]:
#             if thirdNum in possible:
#                 answer += 1
# print(answer)