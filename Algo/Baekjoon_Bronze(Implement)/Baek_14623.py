import sys

a = int(sys.stdin.readline().strip(), 2)
b = int(sys.stdin.readline().strip(), 2)

print(bin(a * b)[2:])