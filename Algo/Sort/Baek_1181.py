import sys
n = int(sys.stdin.readline())

word = []

for _ in range(n):
    word.append(sys.stdin.readline().strip())

word = list(set(word))
word.sort()
word.sort(key=len)

for i in word:
    print(i)
