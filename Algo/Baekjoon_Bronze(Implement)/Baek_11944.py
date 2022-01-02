import sys

n, m = map(int, sys.stdin.readline().split())
result = ''

for _ in range(n):
    result += str(n)

print(result[:m])