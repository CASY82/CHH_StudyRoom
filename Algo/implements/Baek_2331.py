import sys

a, p = map(int, sys.stdin.readline().split())

num_arr = []
num_arr.append(a)

while True:
    a_str = str(a)
    next_num = 0
    for i in range(len(a_str)):
        next_num += int(a_str[i]) ** p

    a = next_num
    if next_num in num_arr:
        break

    num_arr.append(next_num)

print(len(num_arr[:num_arr.index(a)]))

#다른 사람 풀이
# import sys
# from math import pow
# sys.setrecursionlimit(250000)
#
#
# def dfs(a):
#     tmp = 0
#     while a > 0:
#         tmp += int(pow((a % 10), p))
#         a = a//10
#     if tmp in visited:
#         i = visited.index(tmp)
#         chk = visited[i::]
#         for j in chk:
#             visited.remove(j)
#         return
#     else:
#         visited.append(tmp)
#     dfs(tmp)
#
#
# a, p = map(int, input().split())
#
# result = 0
# visited = []
# visited.append(a)
# dfs(a)
#
# print(len(visited))