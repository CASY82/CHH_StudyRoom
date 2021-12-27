import sys

n = int(sys.stdin.readline())
time = list(map(int, sys.stdin.readline().split()))
time_sum = []
time.sort()

for i in range(len(time)):
    time_sum.append(sum(time[:i+1]))

print(sum(time_sum))