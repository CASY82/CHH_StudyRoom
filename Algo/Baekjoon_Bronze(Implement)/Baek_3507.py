import sys

n = int(sys.stdin.readline())
res = 0

if n <= 198:
    for i in range(1, 100):
        for j in range(1, 100):
            if n - i - j == 0:
                res += 1

print(res)