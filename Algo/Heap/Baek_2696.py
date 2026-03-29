# 중앙값 구하기
import sys
import heapq

t = int(sys.stdin.readline())

for _ in range(t):
    m = int(sys.stdin.readline())
    nums = []
    while len(nums) < m:
        nums.extend(map(int, input().split()))

    left = [] # 최대 힙
    right = [] # 최소 힙
    res = []

    for i, num in enumerate(nums):
        if not left or num <= -left[0]:
            heapq.heappush(left, -num)
        else:
            heapq.heappush(right, num)

        if len(left) > len(right) + 1:
            heapq.heappush(right, -heapq.heappop(left))
        elif len(right) > len(left):
            heapq.heappush(left, -heapq.heappop(right))

        if i % 2 == 0:
            res.append(-left[0])

    print(len(res))
    for i in range(0, len(res), 10):
        print(*res[i:i + 10])