import sys

n = int(sys.stdin.readline())
plates = list(map(int, sys.stdin.readline().split()))

tmp = [0] * (max(plates) + 1)

for i in range(len(plates)):
    tmp[plates[i]] += 1

print(max(tmp))

# 다른 사람 풀이
# n=int(input())
# d=dict()
# for x in input().split():
#     if x in d:
#         d[x]+=1
#     else:
#         d[x]=1
# print(max(d.values()))