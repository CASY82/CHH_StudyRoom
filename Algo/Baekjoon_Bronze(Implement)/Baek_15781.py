import sys

n, m = map(int, sys.stdin.readline().split())
helmet = list(map(int, sys.stdin.readline().split()))
jacket = list(map(int, sys.stdin.readline().split()))

print(max(helmet)+max(jacket))