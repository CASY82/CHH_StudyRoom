import sys

n, l, h = map(int, sys.stdin.readline().split())
score = list(map(int, sys.stdin.readline().split()))

score.sort()

tmp = score[l:n - h]

print(sum(tmp) / len(tmp))

# 다른 사람 풀이

# a,b,c=map(int,input().split())
# l=[*map(int,input().split())]
#
# for i in range(b):
#     del l[l.index(min(l))]
# for i in range(c):
#     del l[l.index(max(l))]
# print(sum(l)/len(l))