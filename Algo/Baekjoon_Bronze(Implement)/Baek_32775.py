import sys

s = int(sys.stdin.readline())
f = int(sys.stdin.readline())

if f < s:
    print("flight")
else:
    print("high speed rail")