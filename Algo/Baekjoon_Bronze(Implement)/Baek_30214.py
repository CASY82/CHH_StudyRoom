import sys

s1, s2 = map(int, sys.stdin.readline().split())

if s1 >= (s2 / 2):
    print("E")
else:
    print("H")