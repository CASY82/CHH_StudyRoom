import sys

while True:
    n = int(sys.stdin.readline())

    if n == 0:
        break

    start, end = 1, 50

    while start <= end:
        mid = (start + end) // 2

        print(mid, end=' ')

        if mid > n:
            end = mid - 1
        elif mid == n:
            break
        else:
            start = mid + 1

    print()