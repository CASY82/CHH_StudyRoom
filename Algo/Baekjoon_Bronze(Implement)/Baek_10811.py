import sys

n, m = map(int, sys.stdin.readline().split())
num_list = [(i+1) for i in range(n)]

for _ in range(m):
    i, j = map(int, sys.stdin.readline().split())

    tmp = num_list[i-1:j]
    tmp.reverse()

    num_list = num_list[:i-1] + tmp + num_list[j:]

print(*num_list)