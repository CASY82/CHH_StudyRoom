# 시간 초과
# import sys
#
# n, m = map(int, sys.stdin.readline().split())
# arr = []
#
# for _ in range(n):
#     arr.append(int(sys.stdin.readline()))
#
# arr.sort()
#
# for i in range(m):
#     find = int(sys.stdin.readline())
#
#     try:
#         print(arr.index(find))
#     except:
#         print(-1)

import sys

def lower_bound(nums, target):
    left, right = 0, len(nums)-1

    while left <= right:
        mid = (left + right) // 2

        if nums[mid] == target:
            if right == mid:
                return mid
            right = mid
        else:
            if nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid - 1

    return -1

n, m = map(int, sys.stdin.readline().split())
arr = []

for _ in range(n):
    arr.append(int(sys.stdin.readline()))

arr.sort()

for i in range(m):
    find = int(sys.stdin.readline())
    print(lower_bound(arr, find))