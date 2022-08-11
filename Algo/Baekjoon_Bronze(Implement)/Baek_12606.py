import sys

n = int(sys.stdin.readline())

for i in range(n):
    words = list(sys.stdin.readline().strip().split())

    words.reverse()

    print("Case #{0}:".format(i+1), *words)