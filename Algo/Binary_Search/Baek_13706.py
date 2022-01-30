import sys

n = int(sys.stdin.readline())

start = 0
end = n

while start <= end:
    mid = (start + end) // 2

    result = n // mid

    if result == mid:
        break

    if result > mid:
        start = mid + 1
    else:
        end = mid - 1

print(mid)