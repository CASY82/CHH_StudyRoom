import sys

n = int(sys.stdin.readline())
assignment = []
max_day = 0

for _ in range(n):
    d, w = map(int, sys.stdin.readline().split())
    if max_day < d:
        max_day = d

    assignment.append((d, w))

assignment.sort(key=lambda x : x[1])
days = [0 for _ in range(max_day+1)]
filtered_list = assignment.copy()

for i in range(max_day, 0, -1):
    max_score = 0
    tuple_to_remove = (-1, -1)
    for j in range(len(filtered_list)):
        if filtered_list[j][0] >= i:
            if max_score < filtered_list[j][1]:
                max_score = filtered_list[j][1]

                tuple_to_remove = (filtered_list[j][0], filtered_list[j][1])

    if tuple_to_remove in filtered_list:
        filtered_list.remove(tuple_to_remove)

    days[i] = max_score

print(sum(days))

#다른 사람 풀이1

# import sys
# I = sys.stdin.readline
#
# n = int(I())
# scores = [0]*1001
# for i in range(n):
#     a,b = map(int,I().split())
#     while a>0 and scores[a]>=b:
#         a -= 1
#     while a>0 and scores[a]<b:
#         c = scores[a]
#         scores[a] = b
#         b = c
#         a -= 1
#         while a>0 and scores[a]>=b:
#             a -= 1
# print(sum(scores))

# 다른 사람 풀이2

# n = int(input())
# li = [tuple(map(int, input().split())) for _ in range(n)]
#
# li.sort()
#
# hwList = []
# result = 0
#
# k = li[-1][0]
#
# for day in range(k, 0, -1):
#   while li and li[-1][0] == day:
#     hwList.append(li.pop()[1])
#
#   if hwList:
#     hwList.sort()
#     result += hwList.pop()
#
# print(result)

