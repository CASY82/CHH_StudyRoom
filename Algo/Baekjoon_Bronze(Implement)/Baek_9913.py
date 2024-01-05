import sys

n = int(sys.stdin.readline())

max_num = dict()

for _ in range(n):
    num = int(sys.stdin.readline())

    if num in max_num:
        max_num[num] += 1
    else:
        max_num[num] = 1

print(max(max_num.values()))