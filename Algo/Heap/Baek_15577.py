# Prosjek
import sys
import heapq

n = int(sys.stdin.readline())

nums = []

for _ in range(n):
    nums.append(int(sys.stdin.readline()))

heapq.heapify(nums)

while len(nums) > 1:
    a = heapq.heappop(nums)
    b = heapq.heappop(nums)

    tmp = (a + b) / 2

    heapq.heappush(nums, tmp)

print(f"{nums[0]:.6f}")