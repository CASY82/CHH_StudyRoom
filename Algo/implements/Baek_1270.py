# import sys
# n = int(sys.stdin.readline())
# war = []

# for _ in range(n):
#     war_dic = dict()
#     war = list(map(int, sys.stdin.readline().split()))
#
#     for i in range(1, war[0]+1):
#         if not war[i] in war_dic:
#             war_dic[war[i]] = 1
#         else:
#             war_dic[war[i]] += 1
#
#     many_man = [k for k,v in war_dic.items() if max(war_dic.values()) == v]
#     if len(many_man) >= 2:
#         result = "SYJKGW"
#     else:
#         if (war_dic[many_man[0]] / war[0] * 100) > 50:
#             result = many_man[0]
#         else:
#             result = "SYJKGW"
#
#     print(result)

import sys
n = int(sys.stdin.readline())
war = []

for _ in range(n):
    result = "SYJKGW"
    war_dic = dict()
    war = list(map(int, sys.stdin.readline().split()))

    for i in range(1, war[0]+1):
        if not war[i] in war_dic:
            war_dic[war[i]] = 1
        else:
            war_dic[war[i]] += 1

        if (war_dic[war[i]] / war[0] * 100) > 50:
            result = war[i]
            break

    print(result)

#카운터를 사용한 풀이. 시간이 훨씬 절약되는 것을 확인했다.
# input = __import__('sys').stdin.readline
# MIS = lambda: map(int,input().split())
# from collections import Counter
#
# for TEST in range(int(input())):
#     n, *arr = MIS()
#     C = Counter(arr)
#     if max(C.values())*2 <= n: print("SYJKGW")
#     else: print(C.most_common(1)[0][0])