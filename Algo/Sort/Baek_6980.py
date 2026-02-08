# Train Swapping
import sys

t = int(sys.stdin.readline())

for _ in range(t):
    cnt = 0
    n = int(sys.stdin.readline())
    nums = list(map(int, sys.stdin.readline().split()))

    for i in range(n):
        for j in range(i + 1, n):
            if nums[i] > nums[j]:
                nums[i], nums[j] = nums[j], nums[i]
                cnt += 1

    print("Optimal train swapping takes {} swaps.".format(cnt))