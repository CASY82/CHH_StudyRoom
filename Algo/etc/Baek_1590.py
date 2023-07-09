import sys

n, t = map(int, sys.stdin.readline().split())

result = 1000000000000

for _ in range(n):
    s, i, c = map(int, sys.stdin.readline().split())

    tmp = s

    for _ in range(c):
        compare = tmp - t
        if compare >= 0:
            if result > compare:
                result = compare
                break

        tmp += i

if result == 1000000000000:
    print(-1)
else:
    print(result)