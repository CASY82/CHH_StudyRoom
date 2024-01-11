# import sys
#
# checker = ["", "BFPV", "CGJKQSXZ", "DT", "L", "MN", "R"]
#
# while True:
#     stack = []
#     word = sys.stdin.readline().strip()
#     last_check = ""
#
#     if word == "":
#         break
#
#     for i in range(len(word)):
#         for j in range(1, 7):
#             if word[i] in checker[j]:
#                 if i == 0:
#                     stack.append(str(j))
#                     last_check = str(j)
#
#                 if stack and last_check != str(j):
#                     stack.append(str(j))
#                     last_check = str(j)
#
#                 break
#             else:
#                 if j == 6:
#                     last_check = ""
#
#     print("".join(stack))

import sys

checker = ["", "BFPV", "CGJKQSXZ", "DT", "L", "MN", "R"]

def compress_list(lst):
    compressed = []  # 압축된 요소를 담을 빈 리스트

    for i in range(len(lst)):
        if i == 0 or lst[i] != lst[i-1]:  # 첫 번째 요소이거나 이전 요소와 다를 때만 추가
            compressed.append(lst[i])

    return compressed

while True:
    stack = []
    word = sys.stdin.readline().strip()
    last_check = ""

    if word == "":
        break

    for i in range(len(word)):
        for j in range(1, 7):
            if word[i] in checker[j]:
                stack.append(str(j))
                break

            if j == 6:
                stack.append("X")

    result = compress_list(stack)
    result = [x for x in result if x != "X"]
    print("".join(result))