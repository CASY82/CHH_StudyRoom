#bisect으로 풀어보았다.
import sys
from bisect import bisect_left, bisect_right

n = int(sys.stdin.readline())
numCard = list(map(int, sys.stdin.readline().split()))
m = int(sys.stdin.readline())
checkNum = list(map(int, sys.stdin.readline().split()))

numCard.sort()

for i in checkNum:
    print(bisect_right(numCard, i)-bisect_left(numCard, i), end=' ')


#진짜배기 코드 첨부. 참고용 소스
# import sys
# from collections import deque
#
# n = int(sys.stdin.readline())
#
# nl=list(map(int,sys.stdin.readline().strip().split()))
#
# snl=set(nl)
#
# m = int(sys.stdin.readline())
#
# ml=list(map(int,sys.stdin.readline().strip().split()))
#
# nl.sort()
#
# def d(a):
#     if a not in snl:
#         return 1
#     l=0
#     r=n-1
#     while l<r:
#         if r==l+1 and nl[l]!=nl[r]:
#             if nl[l]==a:
#                 return l
#             elif nl[r]==a:
#                 return r
#
#         elif r==l+1 and nl[l]==nl[r]:
#             return l
#
#         mid = (l+r)//2
#
#         if nl[mid]>a:
#             r=mid-1
#         elif nl[mid]<a:
#             l=mid+1
#         else:
#             r=mid
#
#     return l
#
#
#
#
#
# def u(a):
#     if a not in snl:
#         return 0
#     l=0
#     r=n-1
#     while l<r:
#         if r==l+1 and nl[l]!=nl[r]:
#             if nl[l]==a:
#                 return l
#             elif nl[r]==a:
#                 return r
#         elif r==l+1 and nl[l]==nl[r]:
#             return r
#
#         mid = (l+r)//2
#
#         if nl[mid] > a:
#             r = mid - 1
#         elif nl[mid] < a:
#             l = mid + 1
#         else:
#             l = mid
#
#     return r
#
# for i in ml:
#     print(u(i)-d(i)+1,end=' ')