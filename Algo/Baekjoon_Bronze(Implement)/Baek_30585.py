import sys

h, w = map(int, sys.stdin.readline().split())

one = 0
zero = 0

for i in range(h):
    hang = sys.stdin.readline().strip()

    one += hang.count("1")
    zero += hang.count("0")

print(min(zero, one))