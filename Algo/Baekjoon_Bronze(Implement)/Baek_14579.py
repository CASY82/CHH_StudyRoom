import sys

a, b = map(int, sys.stdin.readline().split())
tmp = 0
result = 0

for i in range(1, a+1):
    tmp += i

result = tmp

for i in range(1, b-a+1):
    tmp = tmp + (a + i)
    result *= tmp

print(result % 14579)