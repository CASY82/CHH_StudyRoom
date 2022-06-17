import sys

n = int(sys.stdin.readline())
price = list(map(int, sys.stdin.readline().split()))

if sum(price)%3 == 0:
    print("yes")
else:
    print("no")