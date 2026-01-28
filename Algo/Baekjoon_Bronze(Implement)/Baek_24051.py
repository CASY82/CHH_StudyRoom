# 알고리즘 수업 - 삽입 정렬(pypy로 통과)
import sys

n, k = map(int, sys.stdin.readline().split())
nums = list(map(int, sys.stdin.readline().split()))

def insertion_sort():
    cnt = 0
    for i in range(1, n):
        loc = i - 1
        next = nums[i]

        while 0 <= loc and next < nums[loc]:
            nums[loc + 1] = nums[loc]
            loc -= 1
            cnt += 1

            if cnt == k:
                return nums[loc + 1]

        if loc + 1 != i:
            nums[loc + 1] = next
            cnt += 1

    return -1

print(insertion_sort())