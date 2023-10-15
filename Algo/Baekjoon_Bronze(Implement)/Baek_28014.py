import sys

n = int(sys.stdin.readline())
tower = list(map(int, sys.stdin.readline().split()))
cnt = 1

tower.reverse()

for i in range(n-1):
    if tower[i] >= tower[i + 1]:
        cnt += 1

print(cnt)

# 다른 사람 풀이
# n = int(input())
# tower = list(map(int, input().split()))
# ans=1
# cnt=0
# for i in range(n-1):
#     if tower[cnt] <= tower[i+1]:
#         cnt=i+1
#         ans+=1
#     else:
#         cnt+=1
# print(ans)