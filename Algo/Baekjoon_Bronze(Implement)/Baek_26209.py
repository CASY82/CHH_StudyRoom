import sys

bit = list(map(int, sys.stdin.readline().split()))

if bit.count(9) > 0:
    print("F")
else:
    print("S")