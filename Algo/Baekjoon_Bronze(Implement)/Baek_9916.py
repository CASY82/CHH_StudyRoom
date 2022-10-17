import sys

n = int(sys.stdin.readline())
tmp = 1

for i in range(1, n+1):
    tmp *= i

print(str(tmp).count("0"))