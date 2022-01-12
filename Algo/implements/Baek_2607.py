# 문제를 다시 이해하여보니 생각보다 간단할거 같다.
# import sys
#
# n = int(sys.stdin.readline())
# compareWord = sys.stdin.readline().strip()
# comparealpha = list(set(compareWord))
# wordList = []
# cnt = 0
#
# for _ in range(n-1):
#     wordList.append(sys.stdin.readline().strip())
#
# for i in range(len(wordList)):
#     if abs(len(list(set(wordList[i]))) - len(comparealpha)) >= 2:
#         continue
#
#     tmp = 0
#     for j in range(len(wordList[i])):
#         if wordList[i][j] not in comparealpha:
#             tmp += 1
#             continue
#
#         if wordList[i][j]
#
#     if tmp >= 2:
#         continue
#     else:
#         cnt += 1
#
# print(cnt)
#
# import sys
#
# n = int(sys.stdin.readline())
# compareWord = sys.stdin.readline().strip()
# compareAlpha = dict()
# compareSet = list(set(compareWord))
# wordList = []
# diffCnt = 0
# result = 0
#
# for i in range(len(compareSet)):
#     compareAlpha[compareSet[i]] = compareWord.count(compareSet[i])
#
# for _ in range(n-1):
#     wordList.append(sys.stdin.readline().strip())
#
# # 두 단어가 같은 구성을 갖는 경우, 또는 한 단어에서 한 문자를 더하거나, 빼거나, 하나의 문자를 다른 문자로 바꾸어 나머지 한 단어와 같은 구성을 갖게 되는 경우에 이들 두 단어를 서로 비슷한 단어
# # 두 개의 단어가 같은 종류의 문자로 이루어져 있다.
# # 같은 문자는 같은 개수 만큼 있다.
# for i in range(len(wordList)):
#     tmp = compareAlpha.copy()
#     for j in range(len(wordList[i])):
#         if wordList[i][j] in tmp:
#             tmp[wordList[i][j]] -= 1
#         else:
#             tmp[wordList[i][j]] = -1

    # # 길이가 다른경우(추가 또는 삭제)
    # if len(compareWord) > len(wordList[i]) or len(compareWord) < len(wordList[i]):
    #     if abs(sum(list(tmp.values()))) < 2:
    #         cnt += 1
    # else: # 길이가 같다. 한문자 치환 가능
    #     if abs(sum(list(tmp.values()))) == 0:
    #         cnt += 1

# import sys
#
# n = int(sys.stdin.readline())
# compareWord = sys.stdin.readline().strip()
# compareAlpha = dict()
# compareSet = list(set(compareWord))
# wordList = []
# result = 0
#
# for i in range(len(compareSet)):
#     compareAlpha[compareSet[i]] = compareWord.count(compareSet[i])
#
# for _ in range(n-1):
#     wordList.append(sys.stdin.readline().strip())
#
# # 두 단어가 같은 구성을 갖는 경우, 또는 한 단어에서 한 문자를 더하거나, 빼거나, 하나의 문자를 다른 문자로 바꾸어 나머지 한 단어와 같은 구성을 갖게 되는 경우에 이들 두 단어를 서로 비슷한 단어
# # 두 개의 단어가 같은 종류의 문자로 이루어져 있다.
# # 같은 문자는 같은 개수 만큼 있다.
# for i in range(len(wordList)):
#     cnt = len(compareWord)
#     for j in range(len(wordList[i])):
#         if wordList[i][j] in compareSet:
#             cnt -= 1
#         else:
#             cnt += 1
#
#     #길이가 다른경우(추가 또는 삭제)
#     if len(compareWord) > len(wordList[i]):
#         if cnt == 1:
#             result += 1
#             print(wordList[i])
#     elif len(compareWord) < len(wordList[i]):
#         if cnt == -1:
#             result += 1
#             print(wordList[i])
#     else: # 길이가 같다. 한문자 치환 가능
#         if cnt == 0 or cnt == 2:
#             result += 1
#             print(wordList[i])
#
#     print(cnt)
# # print(result)

import sys
from collections import Counter

n = int(sys.stdin.readline())
compareWord = sys.stdin.readline().strip()
generalWord = Counter(compareWord)
wordList = []
cnt = 0

for _ in range(n-1):
    wordList.append(sys.stdin.readline().strip())

for i in range(len(wordList)):
    tmp = Counter(wordList[i])

    if len(list((tmp - generalWord).elements())) < 2 and len(wordList[i]) >= len(compareWord):
        cnt += 1
    elif len(list((generalWord - tmp).elements())) < 2 and len(wordList[i]) < len(compareWord):
        cnt += 1

print(cnt)