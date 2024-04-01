import sys

n = int(sys.stdin.readline())
result = True


for _ in range(3):
    nums = list(map(int, sys.stdin.readline().split()))

    if 7 not in nums:
        result = False
        break

if result:
    print(777)
else:
    print(0)