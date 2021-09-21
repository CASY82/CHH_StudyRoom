n, m = map(int, input().split())
square = []

for i in range(n):
    square.append(list(input()))

point = 0

if m != 1 and n != 1:
    for i in range(n - 1):
        for j in range(m - 1):
            if n < m:
                # print('i = ' + str(i) + ' j = ' + str(j))
                for k in range(m - j):
                    # print('k = ' + str(k))
                    if i + k >= n or j + k >= m:
                        break
                    if square[i][j] == square[i][j + k] and square[i][j] == square[i + k][j + k] and square[i][j] == square[i + k][j]:
                        if point <= k:
                            point = k + 1
            else:
                # print('i = ' + str(i) + ' j = ' + str(j))
                for k in range(n - j):
                    # print('k = ' + str(k))
                    if i + k >= n or j + k >= m:
                        break
                    if square[i][j] == square[i][j + k] and square[i][j] == square[i + k][j + k] and square[i][j] == square[i + k][j]:
                        if point <= k:
                            point = k + 1
else:
    point = 1

print(point * point)

'''
3 3
122
221
112
답 : 1

2 3
222
222
답 : 4

4 4
1234
1234
1255
1255
답 : 4

4 4
1234
5068
1234
5678
답 : 1

5 5
40013
10077
88888
66661
91002
답 : 4

1 1
1
답 : 1
'''

# 다른 사람 풀이
# import sys
# N, M = map(int, sys.stdin.readline().split())
# Rectangle = [list(map(int, sys.stdin.readline().strip())) for _ in range(N)]
# size = 1
# for l in range(1, min(N, M)):
#     for row in range(N-l):
#         for col in range(M-l):
#             if Rectangle[row][col] == Rectangle[row+l][col] == Rectangle[row][col+l] == Rectangle[row+l][col+l]:
#                 size = (l+1)**2
# print(size)