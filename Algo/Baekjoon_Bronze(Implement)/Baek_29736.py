# 브실이와 친구가 되고 싶어
import sys

a, b = map(int, sys.stdin.readline().split())
k, x = map(int, sys.stdin.readline().split())

res = 0

for i in range(a, b + 1):
    if x >= abs(i - k):
        res += 1

if res == 0:
    print("IMPOSSIBLE")
else:
    print(res)