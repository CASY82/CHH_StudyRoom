import sys

n = int(sys.stdin.readline())

time = []

for _ in range(n):
    a, b = map(int, sys.stdin.readline().split())

    time.append(a-b)

if len(time) % 2 == 1:
    print(1)
else:
    time.sort()

    print(time[len(time)//2] - time[(len(time)//2)-1] + 1)