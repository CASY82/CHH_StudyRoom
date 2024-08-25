import sys

n, b = map(int, sys.stdin.readline().split())

cows = []

for _ in range(n):
    cows.append(int(sys.stdin.readline()))

cows.sort(reverse=True)
cnt = 0
tmp = 0

for i in range(n):
    tmp += cows[i]
    cnt += 1

    if tmp >= b:
        break

print(cnt)

# 다른 사람 풀이

# import sys
# input = sys.stdin.readline
#
# n, h = map(int, input().split())
# cows = sorted(map(int, [input() for _ in range(n)]))
# s, c = 0, 0
#
# while s<h:
#     s += cows.pop()
#     c += 1
#
# print(c)