import sys

t = int(sys.stdin.readline())

for _ in range(t):
    a, b = sys.stdin.readline().strip().split()

    if int(a) + int(b) > 50:
        print(1)
    else:
        print(int(a) + int(b) - 1)