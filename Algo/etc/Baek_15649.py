import sys
from itertools import permutations

n, m = map(int, sys.stdin.readline().split())

num = [i+1 for i in range(n)]

result = list(map(list, permutations(num, m)))

for i in range(len(result)):
    for j in range(m):
        print(result[i][j], end=' ')
    print()

#백트랙킹으로 푸는 방법
# n, m = list(map(int, input().split()))
#
# visited = [False] * (n + 1)
# tmp = []
#
#
# def backtrack(n, deep, tmp, visited):
#     if deep == m:
#         out = ""
#         for k in tmp:
#             out += str(k) + " "
#         print(out[:-1])
#         return
#
#     for i in range(1, n + 1):
#         if not visited[i]:
#             tmp.append(i)
#             visited[i] = True
#             backtrack(n, deep + 1, tmp, visited)
#             tmp.pop()
#             visited[i] = False
#
#
# backtrack(n, 0, tmp, visited)

# 다른 풀이
# import sys
# input = sys.stdin.readline
#
# A, B = map(int, input().split())
#
# l = []
#
# def back():
#   if len(l) == B:
#     print(' '.join(map(str, l)))
#     return
#
#   for i in range(1, A+1):
#     if i not in l:
#       l.append(i)
#       back()
#       l.pop()
#
#
#
# back()