import sys

n = int(sys.stdin.readline())
cows = list(map(int, sys.stdin.readline().split()))

cows.sort(reverse = True)
line = 0

for i in range(n):
    if cows[i] >= line:
        line += 1

print(line)