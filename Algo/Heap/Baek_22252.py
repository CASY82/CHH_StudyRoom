import sys
import heapq

q = int(sys.stdin.readline())
seller = dict()
res = 0

for _ in range(q):
    command = list(sys.stdin.readline().strip().split())

    if command[0] == "1":
        tmp = []
        for i in range(int(command[2])):
            tmp.append(-int(command[i + 3]))

        if command[1] not in seller:
            seller[command[1]] = tmp
        else:
            for data in tmp:
                heapq.heappush(seller[command[1]], data)
    else:
        if command[1] in seller and seller[command[1]]:
            available = min(int(command[2]), len(seller[command[1]]))
            for i in range(available):
                res += -heapq.heappop(seller[command[1]])

print(res)

# 다른 사람 코드
# import heapq, sys
# from collections import defaultdict
#
# q = int(input())
# dic = defaultdict(list)
# answer = 0
# for _ in range(q):
#     quest = list(input().split())
#
#     if quest[0] == '1':
#         for i in range(int(quest[2])):
#             heapq.heappush(dic[quest[1]], -int(quest[3+i]))
#     else:
#         if dic[quest[1]]:
#             for _ in range(min(int(quest[2]), len(dic[quest[1]]))):
#                 answer += -heapq.heappop(dic[quest[1]])
#
# print(answer)