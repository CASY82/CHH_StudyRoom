import sys

n = int(sys.stdin.readline())
interesting = list(map(int, sys.stdin.readline().split()))
myview = list(map(int, sys.stdin.readline().split()))
nomyview = 0

print(sum(interesting))

for i in range(n):
    if myview[i] == 0:
        nomyview += interesting[i]

print(nomyview)