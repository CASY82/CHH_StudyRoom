import sys

n = int(sys.stdin.readline())

a_dict = {}
b_dict = {}
states = set()
res = 0

for _ in range(n):
    a = sys.stdin.readline().strip()

    if a not in a_dict:
        a_dict[a] = 1
    else:
        a_dict[a] += 1

    states.add(a)

for _ in range(n):
    b = sys.stdin.readline().strip()

    if b not in b_dict:
        b_dict[b] = 1
    else:
        b_dict[b] += 1

    states.add(b)

for state in states:
    if state in a_dict and state in b_dict:
        res += min(a_dict[state], b_dict[state])

print(res)

# 다른 사람 풀이
# from sys import stdin
# R = stdin.readline
#
# d = {}
# n,r = int(R()),0
# for _ in range(n):
#     x = R()
#     if x not in d: d[x] = 0
#     d[x] += 1
# for _ in range(n):
#     x = R()
#     if x in d and d[x]:
#         d[x] -= 1
#         r += 1
# print(r)