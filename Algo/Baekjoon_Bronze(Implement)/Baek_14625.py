import sys

t = int(sys.stdin.readline())
n = int(sys.stdin.readline())
f = list(map(int, sys.stdin.readline().split()))

tmp = sum(f)
if tmp >= t:
    print("Padaeng_i Happy")
else:
    print("Padaeng_i Cry")