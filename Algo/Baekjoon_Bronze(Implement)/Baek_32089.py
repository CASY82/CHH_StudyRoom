import sys

while True:
    n = int(sys.stdin.readline())

    if n == 0:
        break

    newbie = list(map(int, sys.stdin.readline().split()))

    start = 0
    end = start + 3
    res = 0

    while end <= len(newbie):
        res = max(res, sum(newbie[start:end]))
        start += 1
        end += 1

    print(res)