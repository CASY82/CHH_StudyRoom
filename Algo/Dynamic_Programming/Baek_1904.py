import sys
# sys.setrecursionlimit(10 ** 6)

n = int(sys.stdin.readline())

arr = [0, 1, 2] + [0] * n
# def func(x, arr):
#     if x == 0:
#         return arr[0]
#
#     if x == 1:
#         return arr[1]
#
#     if x == 2:
#         return arr[2]
#
#     if arr[x] != 0:
#         return arr[x]
#
#     arr[x] = (func(x-1, arr) + func(x-2, arr)) % 15746
#     return arr[x]
#
# print(func(n, arr))

for i in range(n+1):
    if i <= 2:
        continue

    arr[i] = (arr[i - 1] + arr[i - 2]) % 15746

print(arr[n])
