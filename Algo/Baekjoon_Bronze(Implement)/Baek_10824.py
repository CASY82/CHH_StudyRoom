import sys

a, b, c, d = sys.stdin.readline().strip().split()

new_ab = a + b
new_cd = c + d

print(int(new_ab) + int(new_cd))