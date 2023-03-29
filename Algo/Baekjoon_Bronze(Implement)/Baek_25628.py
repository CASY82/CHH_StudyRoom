import sys

bread, patty = map(int, sys.stdin.readline().split())

bread //= 2

print(min(bread, patty))