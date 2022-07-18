import sys

n = int(sys.stdin.readline())
names = []

for _ in range(n):
    names.append(list(sys.stdin.readline().strip().split()))

names.sort(key = lambda x : (x[1], x[0]))

for i in names:
    print(" ".join(i))