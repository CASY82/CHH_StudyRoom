import sys

n = int(sys.stdin.readline())
time = []

for _ in range(n):
    time.append(list(map(int, sys.stdin.readline().split())))

time.sort(key= lambda x : (x[0], x[1], x[2]))

for i in range(n):
    print(*time[i])