import sys

a, b = map(int, sys.stdin.readline().split())

if a > b:
    a, b = b, a

if a != b:
    print(b-a-1)
else:
    print(0)
for i in range(a+1, b):
    print(i, end=" ")