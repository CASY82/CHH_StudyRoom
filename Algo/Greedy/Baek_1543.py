# import sys
#
# document = sys.stdin.readline().strip()
# searchWord = sys.stdin.readline().strip()
#
# i = 0
# j = 0
# cnt = 0
#
# while True:
#     if i == len(document):
#         break
#
#     if document[i] == searchWord[j]:
#         i += 1
#         j += 1
#
#         if j == len(searchWord):
#             cnt += 1
#             j = 0
#
#         continue
#
#     else:
#         i -= j - 1
#         j = 0
#         if document[i] == searchWord[j]:
#             j += 1
#
#     i += 1
#
# print(cnt)

import sys

document = sys.stdin.readline().strip()
searchWord = sys.stdin.readline().strip()

cnt = 0
i = 0

while i <= len(document)-len(searchWord):
    check = False
    for j in range(len(searchWord)):
        if document[i + j] == searchWord[j]:
            check = True
        else:
            check = False
            break

    if check:
        cnt += 1
        i = i + j + 1
        continue

    i += 1

print(cnt)