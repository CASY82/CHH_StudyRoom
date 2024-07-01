import sys
import itertools

num = sys.stdin.readline().strip()
check = True
permutations = [''.join(p) for p in itertools.permutations(num)]

permutations.sort()

for permu in permutations:
    if num < permu:
        print(permu)
        check = False
        break

if check:
    print(0)

# 다른 사람 풀이
# def solve(arr):
#     i = len(arr) - 1
#     while i > 0 and arr[i - 1] >= arr[i]:
#         i -= 1
#     if i <= 0:
#         return False
#
#     j = len(arr) - 1
#     while arr[j] <= arr[i - 1]:
#         j -= 1
#
#     arr[i - 1], arr[j] = arr[j], arr[i - 1]
#
#     arr[i:] = arr[i:][::-1]
#     return True
#
#
# X = int(input())
# arr = list(str(X))
# if solve(arr):
#     print(int(''.join(arr)))
# else:
#     print(0)