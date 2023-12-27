import sys

n = int(sys.stdin.readline())

for _ in range(n):
    name = sys.stdin.readline().strip()

    if "S" in name:
        print(name)