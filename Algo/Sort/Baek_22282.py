# import sys
#
# n = int(sys.stdin.readline())
# essay = []
# res = 1
#
# for _ in range(n):
#     essay.append(int(sys.stdin.readline()))
#
# for i in range(1, max(essay)):
#     cnt = 0
#     for j in range(n):
#         if i <= essay[j]:
#             cnt += 1
#
#         if cnt >= i:
#             res = max(res, i)
#             break
#
# print(res)

import sys

n = int(sys.stdin.readline())
citations = [int(sys.stdin.readline()) for _ in range(n)]

citations.sort(reverse=True)

h_index = 0
for i in range(n):
    if citations[i] >= i + 1:
        h_index = i + 1
    else:
        break

print(h_index)
