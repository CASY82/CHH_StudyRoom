import sys

n = int(sys.stdin.readline())
cnt = 1

for i in range(1, n):
    if "50" in str(i):
        cnt += 2
    else:
        cnt += 1

print(cnt)

# 다른 사람 풀이

# n= int(input())
# ans=0
# for i in range(0,n):
#     ans+=1
#     if '50' in str(i):
#         ans+=1
#
# print(ans)