# 당연히 시간초과
# import sys
#
# n = int(sys.stdin.readline())
# tree = list(map(int, sys.stdin.readline().split()))
#
# tree.sort(reverse=True)
#
# cnt = 1
# limit = 1
# no_check = 0
#
# while sum(tree) != 0:
#     for i in range(limit):
#         if tree[i] > 0:
#             tree[i] -= 1
#
#     if limit < len(tree):
#         limit += 1
#
#     cnt += 1
#
# print(cnt+1)
#
import sys

n = int(sys.stdin.readline())
tree = list(map(int, sys.stdin.readline().split()))

tree.sort(reverse=True)

cnt = 1
check = tree[0]
i = 1

while check > 0:
    if i == len(tree):
        cnt += check
        break
    else:
        if check <= tree[i]:
            check = tree[i]
        else:
            check -= 1

        cnt += 1
        if i < len(tree):
            i += 1

print(cnt+1)