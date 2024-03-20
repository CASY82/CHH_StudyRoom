import sys

n = int(sys.stdin.readline())
levels = list(map(int, sys.stdin.readline().split()))

def checkLev(lev):
    if lev < 250:
        print(4, end="")
    elif 250 <= lev < 275:
        print(3, end="")
    elif 275 <= lev < 300:
        print(2, end="")
    elif 300 <= lev:
        print(1, end="")

for i in range(n):
    if i != n - 1:
        checkLev(levels[i])
        print(end=" ")
    else:
        checkLev(levels[i])