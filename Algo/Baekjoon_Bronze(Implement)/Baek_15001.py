import sys

n = int(sys.stdin.readline())
stop = []
res = 0

for _ in range(n):
    stop.append(int(sys.stdin.readline()))

stop.sort()

for i in range(n-1):
    res += (stop[i + 1] - stop[i]) ** 2

print(res)