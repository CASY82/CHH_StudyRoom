import sys

num = list(map(int, sys.stdin.readline().split()))

print(num[0] * max(num[1], num[2]) // min(num[1], num[2]))