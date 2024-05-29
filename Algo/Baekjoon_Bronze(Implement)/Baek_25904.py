import sys

n, x = map(int, sys.stdin.readline().split())
limit = list(map(int, sys.stdin.readline().split()))

index = 0

while True:
    if limit[index % n] < x:
        print((index % n) + 1)
        break

    x += 1
    index += 1