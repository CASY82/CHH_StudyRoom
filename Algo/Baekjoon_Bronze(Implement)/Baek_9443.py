# import sys
#
# n = int(sys.stdin.readline())
# cnt = 0
# res = 0
# index = 0
# alpha = "A B C D E F G H I J K L M N O P Q R S T U V W X Y Z".split(" ")
#
# titles = []
#
# for _ in range(n):
#     title = sys.stdin.readline().strip()
#
#     titles.append(title)
#
# titles.sort()
#
# for i in range(n):
#     if titles[i][0] == alpha[index]:
#         index += 1
#         cnt += 1
#     else:
#         res = max(res, cnt)
#
#         if titles[i][0] == "A":
#             cnt = 1
#             index = 1
#         else:
#             cnt = 0
#             index = 0
#
# res = max(res, cnt)
#
# print(res)

import sys

n = int(sys.stdin.readline())
alpha = "A B C D E F G H I J K L M N O P Q R S T U V W X Y Z".split(" ")
tmp = set()
res = 0

for _ in range(n):
    title = sys.stdin.readline().strip()

    tmp.add(title[0])

title_first = list(tmp)
title_first.sort()

for i in range(len(title_first)):
    if title_first[i] == alpha[i]:
        res += 1

print(res)