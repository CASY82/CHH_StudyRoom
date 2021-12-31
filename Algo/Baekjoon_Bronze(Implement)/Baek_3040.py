import sys

smallP = [int(sys.stdin.readline()) for _ in range(9)]

for i in range(9):
    for j in range(9):
        result = smallP.copy()
        if i == j:
            continue
        else:
            result.remove(smallP[i])
            result.remove(smallP[j])

        if sum(result) == 100:
            break

    if sum(result) == 100:
        break

for i in result:
    print(i)

# 조합으로 할까 하다가 안했는데... 조합으로 풀면 이렇게된다.

# from sys import stdin
# from itertools import permutations
# input = stdin.readline
#
# a = [int(input()) for _ in range(9)]
#
# for x in permutations(a, 7):
#     if sum(x) == 100:
#         print(*x, sep = '\n')
#         break