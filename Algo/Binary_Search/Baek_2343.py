import sys

n, m = map(int, sys.stdin.readline().split())
lecture = list(map(int, sys.stdin.readline().split()))

end = sum(lecture)
start = max(lecture)

while start <= end:
    mid = (start + end) // 2
    tmp = 0
    cnt = 0

    for i in lecture:
        tmp += i
        if tmp > mid:
            tmp = i
            cnt += 1
        if tmp == mid:
            tmp = 0
            cnt += 1

    if tmp < mid and tmp != 0:
        cnt += 1

    if cnt > m:
        start = mid + 1
    else:
        end = mid - 1

print(start)

#참고 소스
# import sys
# input=sys.stdin.readline
# from collections import deque
#
# n,m=map(int,input().split())
#
# lesson=list(map(int,input().split()))
# l=max(lesson)
# r=sum(lesson)
# ans=sys.maxsize
# while l<=r:
#     mid=(l+r)//2
#     cnt=0
#     sum=0
#     for i in range(len(lesson)):
#         if sum+lesson[i]>mid:
#             cnt+=1
#             sum=0
#         sum+=lesson[i]
#     if sum:
#         cnt+=1
#
#     if cnt>m: # 블루레이 개수가 m보다 커 (각 크기가 작음)
#         l=mid+1
#     else:
#         ans=min(ans,mid)
#         r=mid-1
# print(ans)