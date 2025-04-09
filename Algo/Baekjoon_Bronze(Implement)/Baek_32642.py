import sys

n = int(sys.stdin.readline())
rainy = list(map(int, sys.stdin.readline().split()))
tmp = 0
res = 0

for i in range(n):
    if rainy[i] == 0:
        tmp -= 1
    else:
        tmp += 1

    res += tmp

print(res)