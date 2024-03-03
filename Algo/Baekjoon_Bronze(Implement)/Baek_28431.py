import sys

array = []

for _ in range(5):
    array.append(int(sys.stdin.readline()))

for i in range(5):
    if array.count(array[i]) - 4 == 1 or array.count(array[i]) - 2 == 1 or array.count(array[i]) == 1:
        print(array[i])
        break

# 다른 사람 풀이
# import sys
# input = sys.stdin.readline
#
# X = set()
# N = 0
# for _ in range(5):
#     a = int(input())
#     if a in X:
#         N -= a
#         X.discard(a)
#     else:
#         X.add(a)
#         N += a
# print(N)

# 다른 사람 풀이 2

# lst = [0]*10
#
# for i in range(5):
#     lst[int(input())] += 1
#
# for i in range(len(lst)):
#     if (lst[i] % 2) == 1:
#         print(i)
#         break
