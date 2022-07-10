import sys

l = int(sys.stdin.readline())

if l % 5 == 0:
    print(l // 5)
else:
    print(l // 5 + 1)