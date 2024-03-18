import sys

n = int(sys.stdin.readline())
numbers = list(map(int, sys.stdin.readline().split()))

standard = numbers.index(-1)

tmp_left = numbers[:standard]
tmp_right = numbers[standard + 1:]

print(min(tmp_right) + min(tmp_left))