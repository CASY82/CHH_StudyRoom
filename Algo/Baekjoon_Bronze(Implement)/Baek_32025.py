import sys

h = int(sys.stdin.readline()) * 100
w = int(sys.stdin.readline()) * 100

print(min(h, w) // 2)