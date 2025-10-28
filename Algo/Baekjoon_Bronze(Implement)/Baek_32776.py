import sys

s = int(sys.stdin.readline())
ma, f, mb = map(int, sys.stdin.readline().split())

tmp = ma + f + mb

if s <= tmp or s <= 240:
    print("high speed rail")
else:
    print("flight")