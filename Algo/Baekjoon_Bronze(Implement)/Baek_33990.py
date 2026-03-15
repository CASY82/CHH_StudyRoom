# 3대 512
import sys

n = int(sys.stdin.readline())
res = -1
diff = 9999999999999999999

for _ in range(n):
    weight = list(map(int, sys.stdin.readline().split()))

    tmp = sum(weight)
    if tmp >= 512:
        if diff > abs(512 - tmp):
            res = tmp
            diff = abs(512 - tmp)

print(res)