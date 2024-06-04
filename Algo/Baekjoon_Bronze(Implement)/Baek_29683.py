import sys

n, a = map(int, sys.stdin.readline().split())
ticket = list(map(int, sys.stdin.readline().split()))

res = 0

for i in range(n):
    res += ticket[i] // a

print(res)