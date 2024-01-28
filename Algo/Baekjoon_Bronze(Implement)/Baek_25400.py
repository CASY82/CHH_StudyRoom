import sys

n = int(sys.stdin.readline())
num_list = list(map(int, sys.stdin.readline().split()))
num = 1
length = len(num_list)

for i in range(length):
    if num_list[i] == num:
        num += 1

print(length - (num - 1))