import sys

nums = list(map(int, sys.stdin.readline().split()))

one_cnt = nums.count(1)
two_cnt = nums.count(2)

if one_cnt > two_cnt:
    print(1)
else:
    print(2)