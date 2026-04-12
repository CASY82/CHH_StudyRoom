# 벼락치기
import sys

n = int(sys.stdin.readline())

if n <= 28:
    for x in range(1, 8):
        if x * (x + 1) // 2 >= n:
            print(x)
            break
else:
    print((n + 27) // 7)