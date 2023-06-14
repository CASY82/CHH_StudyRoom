import sys

n, a, b = map(int, sys.stdin.readline().split())

if a > b:
    print("Subway")
elif a < b:
    print("Bus")
else:
    print("Anything")