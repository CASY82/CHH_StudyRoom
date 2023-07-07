import sys

n = int(sys.stdin.readline())
nums = list(map(int, sys.stdin.readline().split()))

nums.sort(reverse=True)

alice = 0
bob = 0

for i in range(n):
    if i % 2 == 0:
        alice += nums[i]
    else:
        bob += nums[i]

print(alice, bob)