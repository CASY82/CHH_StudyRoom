import sys

n = int(sys.stdin.readline())
word = []

for _ in range(n):
    word.append(sys.stdin.readline().strip())

for i in word:
    if i[::-1] in word:
        print(len(i), i[len(i)//2])
        break