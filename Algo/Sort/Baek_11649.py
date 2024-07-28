import sys

n = int(sys.stdin.readline())
word = []

for _ in range(n):
    word.append(sys.stdin.readline().strip()[::-1])

word.sort()

for w in word:
    print(w)