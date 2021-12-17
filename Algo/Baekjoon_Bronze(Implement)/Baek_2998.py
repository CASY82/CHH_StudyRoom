import sys

word = sys.stdin.readline().strip()

if len(word) % 3 != 0:
    word = '0'*(3 - (len(word) % 3)) + word

word = [word[i:i+3] for i in range(0, len(word), 3)]

for i in word:
    print(int(i, 2), end='')