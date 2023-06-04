import sys

n = int(sys.stdin.readline())
result = 0

for _ in range(n):
    filename = sys.stdin.readline().strip().split(".")

    if len(filename) == 2:
        if 0 < len(filename[0]) <= 8 and 0 < len(filename[1]) <= 3:
            result += 1

print(result)