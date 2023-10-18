import sys

n = int(sys.stdin.readline())
check = n * ((n * n) + 1) // 2

num_check = [1] + [0 for _ in range(n * n)]
matrix = []

for _ in range(n):
    matrix.append(list(map(int, sys.stdin.readline().split())))

for i in range(n):
    for j in range(n):
        num_check[matrix[i][j]] = 1

row_sums = [sum(row) for row in matrix]
col_sums = [sum(col) for col in zip(*matrix)]
main_diag_sum = sum(matrix[i][i] for i in range(min(len(matrix), len(matrix[0]))))
secondary_diag_sum = sum(matrix[i][len(matrix) - 1 - i] for i in range(min(len(matrix), len(matrix[0]))))

row_check = False
col_check = False

for i, row_sum in enumerate(row_sums):
    if row_sum != check:
        row_check = True
        break

for j, col_sum in enumerate(col_sums):
    if col_sum != check:
        col_check = True
        break

if row_check or col_check or secondary_diag_sum != check or main_diag_sum != check or sum(num_check) != (n * n) + 1:
    print("FALSE")
else:
    print("TRUE")

# 다른 사람 풀이
# def has_duplicates(a):
#     return len(a) != len(set(a))
#
# n = int(input())
# m = n * ( n**2 + 1)/2
# arr = [list(map(int,input().split())) for _ in range(n)]
# arr_chk = sum(arr,[])
# chk = True
#
#
# if(has_duplicates(arr_chk) == True):
#     print("FALSE")
#     chk = False
#
#
# if chk:
#     for i in range(n):
#         tmp_x = 0
#         for j in range(n):
#             tmp_x += arr[i][j]
#         if tmp_x != m:
#             chk = False
#             print("FALSE")
#             break
#
# if chk:
#     for a in range(n):
#         tmp_y = 0
#         for b in range(n):
#             tmp_y += arr[b][a]
#         if tmp_y != m:
#             chk = False
#             print("FALSE")
#             break
#
# if chk:
#     tmp_1 = 0
#     for k in range(n):
#         tmp_1 += arr[k][k]
#     if tmp_1 != m:
#         chk = False
#         print("FALSE")
#
# if chk:
#     tmp_2 = 0
#     for l in range(n-1,-1,-1):
#         tmp_2 += arr[l][l]
#     if tmp_2 != m:
#         chk = False
#         print("FALSE")
#
# if chk:
#     print("TRUE")