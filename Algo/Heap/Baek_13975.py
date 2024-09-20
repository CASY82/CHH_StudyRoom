import sys
import heapq

t = int(sys.stdin.readline())

for _ in range(t):
    res = 0
    n = int(sys.stdin.readline())
    nums = list(map(int, sys.stdin.readline().split()))
    heapq.heapify(nums)

    while len(nums) > 1:
        first = heapq.heappop(nums)
        second = heapq.heappop(nums)

        merge = first + second
        res += merge

        heapq.heappush(nums, merge)

    print(res)