import sys

n = int(sys.stdin.readline())

tmp = format(n, 'b')
rev = "0b" + "".join(reversed(tmp))

print(int(rev, 2))