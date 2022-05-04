import sys

n = int(sys.stdin.readline())

count = 0
interval_sum = 0
end = 1

for start in range(1, n+1):
    while interval_sum < n and end <= n:
        interval_sum += end
        end += 1

    if interval_sum == n:
        count += 1

    interval_sum -= start

print(count)