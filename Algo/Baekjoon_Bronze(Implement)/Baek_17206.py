import sys

t = int(sys.stdin.readline())
num_list = list(map(int, sys.stdin.readline().split()))

max_number = max(num_list)
memo = [0] * (max_number + 1)

for i in range(1, max_number + 1):
    memo[i] = memo[i - 1]
    if i % 3 == 0 or i % 7 == 0:
        memo[i] += i

for num in num_list:
    print(memo[num])