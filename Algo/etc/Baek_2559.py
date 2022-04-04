import sys

n, k = map(int, sys.stdin.readline().split())

degrees = list(map(int, sys.stdin.readline().split()))

max_degrees = -10000000
interval_sum = 0
end = 0

for start in range(n):
    if end == n:
        break

    while end < k + start:
        interval_sum += degrees[end]
        end += 1

    if interval_sum > max_degrees:
        max_degrees = interval_sum
    interval_sum -= degrees[start]

print(max_degrees)