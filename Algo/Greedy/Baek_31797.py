import sys

n = int(sys.stdin.readline())
need_solve = list(map(int, sys.stdin.readline().split()))

problem = [[] for _ in range(5)]

for _ in range(n):
    level, time = map(int, sys.stdin.readline().split())

    if level == 1:
        problem[0].append(time)
    elif level == 2:
        problem[1].append(time)
    elif level == 3:
        problem[2].append(time)
    elif level == 4:
        problem[3].append(time)
    elif level == 5:
        problem[4].append(time)

for i in range(5):
    problem[i].sort()

res = 0

for index, check in enumerate(need_solve):
    for j in range(check):
        if j == 0:
            tmp = problem[index][j]
        else:
            tmp = problem[index][j] - problem[index][j - 1] + problem[index][j]

        res += tmp

    if index != len(need_solve) - 1:
        res += 60

print(res)

# 다른 사람 풀이
# import sys
#
# def get_ans():
#     input = sys.stdin.readline
#     N = int(input())
#     p_list = list(map(int, input().split()))
#     dic = {}
#     for _ in range(N):
#         k, t = map(int, input().split())
#         try:
#             dic[k].append(t)
#         except:
#             dic[k] = [t]
#     ans = -60
#     for key, value in dic.items():
#         value.sort()
#     for idx, i in enumerate(p_list):
#         if i != 0:
#             ans += 60
#             before = dic[idx+1][0]
#             for j in range(i):
#                 time = dic[idx+1][j]
#                 ans += abs(time-before) + time
#                 before = time
#     return ans
#
#
# print(get_ans())