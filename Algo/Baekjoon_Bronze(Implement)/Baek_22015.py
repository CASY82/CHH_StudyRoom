import sys

a, b, c = map(int, sys.stdin.readline().split())

max_candy = max(a, b, c)

print(max_candy - a + max_candy - b + max_candy - c)