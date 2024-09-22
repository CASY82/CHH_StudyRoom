import sys

n = int(sys.stdin.readline())
menu = []

for _ in range(n):
    menu.append(int(sys.stdin.readline()))

m = int(sys.stdin.readline())
total = 0

for _ in range(m):
    total += menu[int(sys.stdin.readline()) - 1]

print(total)