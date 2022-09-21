import sys

n = int(sys.stdin.readline())

print("Gnomes:")
for _ in range(n):
    length = list(map(int, sys.stdin.readline().split()))

    desc = sorted(length)
    asc = sorted(length, reverse=True)

    if desc == length or asc == length:
        print("Ordered")
    else:
        print("Unordered")