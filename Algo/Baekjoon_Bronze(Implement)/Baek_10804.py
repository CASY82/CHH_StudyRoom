import sys

num = [(i+1) for i in range(20)]

for i in range(10):
    start, end = map(int, sys.stdin.readline().split())

    for i in range(abs(end-start)//2+1):
        num[start + i - 1], num[end - i - 1] = num[end - i - 1], num[start + i - 1]

print(*num)