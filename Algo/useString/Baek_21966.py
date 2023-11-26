import sys

n = int(sys.stdin.readline())

sentence = sys.stdin.readline().strip()

if n <= 25:
    print(sentence)
else:
    tmp = sentence[11:len(sentence)-11].split(".")
    if len(tmp) == 1 or tmp[1] == "":
        print(sentence[:11] + "..." + sentence[len(sentence)-11:])
    else:
        print(sentence[:9] + "......" + sentence[len(sentence)-10:])

# 다른 사람 풀이
# N = int(input())
# S = input()
#
# if len(S) <= 25:
#     print(S)
# else:
#     front = S[:11]
#     rear = S[-11:]
#     center = S[11:-11]
#     for i in range(len(center) - 1):
#         if ord(center[i]) == 46:
#             center = "......"
#             front = S[:9]
#             rear = S[-10:]
#             print(front + center + rear)
#             break
#     else:
#         center = "..."
#         print(front + center + rear)