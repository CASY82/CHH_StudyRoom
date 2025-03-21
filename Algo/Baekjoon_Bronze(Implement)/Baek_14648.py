import sys

n, q = map(int, sys.stdin.readline().split())

nums = list(map(int, sys.stdin.readline().split()))

for _ in range(q):
    command = list(map(int, sys.stdin.readline().split()))

    if command[0] == 1:
        print(sum(nums[command[1] - 1:command[2]]))
        nums[command[1] - 1], nums[command[2] - 1] = nums[command[2] - 1], nums[command[1] - 1]
    elif command[0] == 2:
        print(sum(nums[command[1] - 1:command[2]]) - sum(nums[command[3] - 1:command[4]]))