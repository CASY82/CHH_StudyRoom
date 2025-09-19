import sys

n = int(sys.stdin.readline())
index = 1
total = 0
res = 0

while True:
    tmp = index ** 2

    if total + tmp <= n:
        index += 2
        total += tmp
        res += 1
    else:
        break

print(res)