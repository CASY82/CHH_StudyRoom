import sys

a, b = map(int, sys.stdin.readline().split())
c, d = map(int, sys.stdin.readline().split())
result = 0

if a + d < b + c:
    result += a + d
else:
    result += b + c

print(result)