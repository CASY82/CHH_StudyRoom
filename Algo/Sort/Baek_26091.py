import sys

n, m = map(int, sys.stdin.readline().split())
power = list(map(int, sys.stdin.readline().split()))
res = 0

power.sort()

end = n - 1
start = 0

while True:
    if start >= end:
        break

    if power[start] + power[end] >= m:
        res += 1
        end -= 1

    start += 1

print(res)