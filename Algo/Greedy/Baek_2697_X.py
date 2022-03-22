# 해당 소스는 틀렸다.
# import sys
#
# t = int(sys.stdin.readline())
#
# for _ in range(t):
#     num = sys.stdin.readline().strip()
#
#     for i in range(len(num)-1, len(num)//2-1, -1):
#         if 0 < i < len(num)-1:
#             if int(num[:i]) < int(num[i:]):
#                 ori = list(num[:i])
#                 tmp = list(num[i:])
#                 check = True
#                 break
#
#     for i in range(len(tmp)-1, -1, -1):
#         if int(tmp[0]) < int(tmp[i]):
#             tmp[0], tmp[i] = tmp[i], tmp[0]
#             break
#
#     new_list = tmp[1:]
#     new_list.sort()
#     tmp = list(tmp[0]) + new_list
#     result = ''.join(ori + tmp)
#
#     if int(result) <= int(num):
#         print("BIGGEST")
#     else:
#         print(result)

import sys

t = int(sys.stdin.readline())
for _ in range(t):
    check = False
    num = list(map(int, sys.stdin.readline().strip()))
    result = ''

    for i in range(len(num)-1, -1, -1):
        if num[i] < num[i-1]:
            continue
        else:
            num[i:] = sorted(num[i:])
            for idx, tmp in enumerate(num[i:]):
                if num[i-1] < tmp:
                    num[i-1], num[idx+i] = num[idx+i], num[i-1]
                    check = True
                    for j in range(len(num)):
                        result += str(num[j])
                    print(result)
                    break
            if check:
                break

    if not check:
        print("BIGGEST")