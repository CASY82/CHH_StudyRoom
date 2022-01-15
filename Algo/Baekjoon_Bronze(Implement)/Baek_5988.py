import sys

n = int(sys.stdin.readline())

for _ in range(n):
    if int(sys.stdin.readline()) % 2 == 0: print("even")
    else: print("odd")