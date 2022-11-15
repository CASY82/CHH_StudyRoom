import sys

n, w, h = map(int, sys.stdin.readline().split())

longest = int((w ** 2 + h ** 2) ** 0.5)

for _ in range(n):
    num = int(sys.stdin.readline())

    if num <= longest:
        print("YES")
    else:
        print("NO")