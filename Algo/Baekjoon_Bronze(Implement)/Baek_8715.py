import sys

n = int(sys.stdin.readline())
num = list(map(int, sys.stdin.readline().split()))

num.sort()

result = True

for i in range(1, n + 1):
    if i != num[i - 1]:
        result = False

if result:
    print("TAK")
else:
    print("NIE")