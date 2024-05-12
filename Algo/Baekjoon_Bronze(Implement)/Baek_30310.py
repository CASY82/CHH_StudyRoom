import sys

n = int(sys.stdin.readline())
forks = list(map(int, sys.stdin.readline().split()))

forks.sort()

print(forks[0] + forks[1])