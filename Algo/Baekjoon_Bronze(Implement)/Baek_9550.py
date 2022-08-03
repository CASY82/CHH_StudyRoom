import sys

t = int(sys.stdin.readline())

for _ in range(t):
    n, k = map(int, sys.stdin.readline().split())

    candy = list(map(int, sys.stdin.readline().split()))

    result = 0

    for cnt in candy:
        result += cnt // k

    print(result)