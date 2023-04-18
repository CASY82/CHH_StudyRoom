import sys

n = int(sys.stdin.readline())

for cnt in range(n):
    rice = list(map(int, sys.stdin.readline().split()))

    rice.sort()

    print("Case #{0}: {1}".format(cnt+1, rice[-1]))