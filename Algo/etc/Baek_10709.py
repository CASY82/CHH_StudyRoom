import sys

h, w = map(int, sys.stdin.readline().split())

result = [[-1 for _ in range(w)] for _ in range(h)]
sky_map = []

for _ in range(h):
    sky_map.append(list(sys.stdin.readline().strip()))

for i in range(h):
    for j in range(w):
        if sky_map[i][j] == "c":
            result[i][j] = 0

        if result[i][j - 1] != -1 and result[i][j] != 0:
            result[i][j] = result[i][j - 1] + 1

for i in range(h):
    print(*result[i])

# 다른 사람 풀이
# h, w = map(int, input().split())
#
# s = []
# c = [[-1 for _ in range(w)] for __ in range(h)]
#
# for i in range(h):
#     a = input()
#     k = []
#     for i in a: k.append(i)
#     s.append(k)
#
# for i in range(h):
#     for j in range(w):
#         if s[i][j] == 'c':
#             cnt = 0
#             try:
#                 for k in range(j, w):
#                     c[i][k] = cnt
#                     cnt += 1
#             except:
#                 pass
#
# for i in c:
#     for j in i:
#         print(j, end=' ')
#     print()