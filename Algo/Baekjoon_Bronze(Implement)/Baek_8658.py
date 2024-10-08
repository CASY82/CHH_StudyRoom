import sys

n = int(sys.stdin.readline())

max_num = n - 1
min_num = 0

for i in range(1, n):
    if n % i != 0:
        min_num = i
        break

print(min_num, max_num)