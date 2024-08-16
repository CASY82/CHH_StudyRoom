import sys

n, m = map(int, sys.stdin.readline().split())
sum_nums = list(map(int, sys.stdin.readline().split()))
multi_nums = list(map(int, sys.stdin.readline().split()))

tmp = sum(sum_nums)

for num in multi_nums:
    if num != 0:
        tmp *= num

print(tmp)