import sys

n = int(sys.stdin.readline())
num = list(map(int, sys.stdin.readline().split()))

num_list = [0 for _ in range(n)]

for i in range(n):
    num_list[i] = 1
    for j in range(i):
        if num[i] > num[j]:
            num_list[i] = max(num_list[i], num_list[j] + 1)

print(max(num_list))