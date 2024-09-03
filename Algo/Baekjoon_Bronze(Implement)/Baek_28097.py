import sys

n = int(sys.stdin.readline())
time = list(map(int, sys.stdin.readline().split()))

total_time = sum(time) + (len(time) - 1) * 8

print(total_time // 24, total_time % 24)