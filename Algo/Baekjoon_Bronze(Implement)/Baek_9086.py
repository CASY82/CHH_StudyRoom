import sys

n = int(sys.stdin.readline())

for _ in range(n):
    word = sys.stdin.readline().strip()

    print(word[0], word[-1], sep='')