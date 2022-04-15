import sys

n = sys.stdin.readline().strip()

n = "0b" + n
n = int(n, 2)

print(format(n*17, 'b'))