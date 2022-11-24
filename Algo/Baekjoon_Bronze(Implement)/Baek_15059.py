import sys

a = list(map(int, sys.stdin.readline().split()))
r = list(map(int, sys.stdin.readline().split()))

result = 0

for i in range(3):
    if a[i] - r[i] < 0:
        result += abs(a[i] - r[i])

print(result)