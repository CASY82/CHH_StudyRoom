import sys

n = int(sys.stdin.readline())
num = list(map(int, sys.stdin.readline().split()))

newNum = [-1000000001]

for i in num:
    if newNum[-1] < i:
        newNum.append(i)
    else:
        start = 0
        end = len(newNum)

        while start < end:
            mid = (start + end) // 2

            if newNum[mid] < i:
                start = mid + 1
            else:
                end = mid

        newNum[end] = i

print(len(newNum)-1)

#아... 이분탐색을 직접 구현하지 않고 bisect을 써도 된다! --> 시간이 더 단축!
# from bisect import bisect_left
#
# n = int(input())
# arr = list(map(int, input().split()))
# lis = [-1000000001]
#
# for i in range(n):
#     if lis[-1] < arr[i]:
#         lis.append(arr[i])
#     else:
#         idx = bisect_left(lis, arr[i])
#         lis[idx] = arr[i]
#
# print(len(lis) - 1)