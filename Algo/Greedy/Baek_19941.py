# import sys
#
# n, k = map(int, sys.stdin.readline().split())
# loc = list(sys.stdin.readline().strip())
# People = []
# Hamberger = []
# for i in range(len(loc)):
#     if loc[i] == "H":
#         Hamberger.append(i+1)
#     else:
#         People.append(i+1)
#
# print(People, Hamberger)
#앞에 있는 사람 순서로, 가장 멀리있는 함바가 먹으면 될듯

import sys

n, k = map(int, sys.stdin.readline().split())
loc = list(sys.stdin.readline().strip())
cnt = 0

for i in range(len(loc)):
    if loc[i] == "P":
        check = True
        for j in range(k, 0, -1):
            if i - j >= 0 and loc[i - j] == "H":
                cnt += 1
                loc[i - j] = "O"
                loc[i] = "D"
                check = False
                break
        if check:
            for j in range(1, k+1):
                if i + j < len(loc) and loc[i + j] == "H":
                    cnt += 1
                    loc[i + j] = "O"
                    loc[i] = "D"
                    break

print(cnt)

#deque로 푸는 법 처음에 stack이나 queue를 쓰면 어떨까 했는데...
# import sys
# from collections import deque
# #19941
# input = sys.stdin.readline
#
#
# N, K = map(int,input().split())
# arr = input().split()[0]
# burger = deque()
# person = deque()
#
# for idx, item in enumerate(arr):
#     if item =='P':
#         person.append(idx)
#     elif item == 'H':
#         burger.append(idx)
#
# ans = 0
#
# while person:
#     personLoc = person.popleft()
#     while burger:
#         burgerLoc = burger.popleft()
#         if abs(burgerLoc - personLoc) <=K:
#             ans += 1
#             break
#         if burgerLoc > personLoc:
#             burger.appendleft(burgerLoc)
#             break
#
# print(ans)