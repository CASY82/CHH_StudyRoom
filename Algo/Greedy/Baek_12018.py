import sys

n, m = map(int, sys.stdin.readline().split())
subject = []
cnt = 0

for _ in range(n):
    p, l = map(int, sys.stdin.readline().split())

    mile = list(map(int, sys.stdin.readline().split()))

    mile.sort(reverse=True)

    if p < l:
        subject.append(1)
    else:
        subject.append(mile[l-1])

subject.sort()

for i in subject:
    if i <= m:
        cnt += 1
        m -= i
    else:
        break

print(cnt)

# heapq쓰는 방식
#import heapq
#
# ans = 0
# n, m = map(int, input().split())
# temp = []
#
# for _ in range(n):
#     P, L = map(int, input().split())
#     mileages = list(map(int, input().split()))
#     heapq.heapify(mileages)
#     num = L - P
#     if num > 0:
#         heapq.heappush(temp, 1)
#     else:
#         for i in range(abs(num)):
#             heapq.heappop(mileages)
#         heapq.heappush(temp, heapq.heappop(mileages))
#
# while temp:
#     mileage = heapq.heappop(temp)
#     if m - mileage >= 0:
#         ans+=1
#         m-= mileage
#     else:
#         break
#
# print(ans)