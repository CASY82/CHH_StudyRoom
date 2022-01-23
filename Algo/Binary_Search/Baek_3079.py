import sys

n, m = map(int, sys.stdin.readline().split())
times = []

for _ in range(n):
    times.append(int(sys.stdin.readline()))

start = 0
end = max(times) * m

while start <= end:
    mid = (start + end) // 2
    total_human = 0

    for i in times:
        total_human += mid // i

    if total_human < m:
        start = mid + 1
    else:
        end = mid - 1

print(start)