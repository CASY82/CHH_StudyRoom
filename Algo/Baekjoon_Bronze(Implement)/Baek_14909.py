import sys

num_arr = list(map(int, sys.stdin.readline().split()))

result = 0

for num in num_arr:
    if num > 0:
        result += 1

print(result)