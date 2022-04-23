import sys

t = int(sys.stdin.readline())

for _ in range(t):
    k = int(sys.stdin.readline())

    result = 1
    cnt = 1

    while cnt < k:
        result += 0.5
        result *= 2
        cnt += 1

    print(int(result))