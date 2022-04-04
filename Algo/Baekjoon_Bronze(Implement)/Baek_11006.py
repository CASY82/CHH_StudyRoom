import sys

t = int(sys.stdin.readline())

for _ in range(t):
    n, m = map(int, sys.stdin.readline().split())

    total_leg = m * 2
    solo_chicken = total_leg - n
    print(solo_chicken, m - solo_chicken)