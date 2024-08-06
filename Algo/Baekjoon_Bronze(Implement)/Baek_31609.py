import sys

n = int(sys.stdin.readline())
number = list(map(int, sys.stdin.readline().split()))

tmp = set(number)
tmp = list(tmp)
tmp.sort()

for numb in tmp:
    print(numb)