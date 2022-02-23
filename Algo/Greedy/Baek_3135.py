import sys

a, b = map(int, sys.stdin.readline().split())
n = int(sys.stdin.readline())
favorite = []
result = 0

for _ in range(n):
    favorite.append(int(sys.stdin.readline()))

if b in favorite:
    result = 1
else:
    min_tmp = 1001
    for i in range(len(favorite)):
        if min_tmp > abs(b - favorite[i]):
            min_tmp = abs(b - favorite[i])

    if min_tmp < abs(a - b):
        result = min_tmp + 1
    else:
        result = abs(a - b)

print(result)