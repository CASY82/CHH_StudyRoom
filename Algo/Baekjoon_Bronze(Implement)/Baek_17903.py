# Counting Clauses
import sys

m, n = map(int, sys.stdin.readline().split())

for _ in range(m):
    nums = list(map(int, sys.stdin.readline().split()))

if m >= 8:
    print("satisfactory")
else:
    print("unsatisfactory")