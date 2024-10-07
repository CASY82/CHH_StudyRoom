import sys

t = int(sys.stdin.readline())

for _ in range(t):
    susic = list(sys.stdin.readline().strip())

    # False면 팩토리얼 True면 논리 반전
    check = False
    num = 0

    if '1' in susic:
        num = 1

    for i in range(len(susic)):
        now = susic.pop()

        # 팩토리얼
        if not check and now == '!':
            num = 1
        # 논리 반전
        elif check and now == '!':
            num = not num
        # 숫자인 경우
        elif now != '!':
            check = not check

    if num:
        print(1)
    else:
        print(0)

# 다른 사람 풀이
# t = int(input())
#
# for i in range(t):
#     a = input()
#     b = 0
#     cnt = 0
#     res = 0
#
#     for j in a:
#         if (b == 0 and j == '!'):
#             cnt += 1
#         elif j.isdigit():
#             res = int(j)
#             b = 1
#         else:
#             res = 1
#
#     if (res == 1):
#         if (cnt % 2 == 0):
#             res = 1
#         else:
#             res = 0
#     else:
#         if (cnt % 2 == 0):
#             res = 0
#         else:
#             res = 1
#     print(res)
