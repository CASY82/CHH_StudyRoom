import sys

mo = ['a', 'e', 'i', 'o', 'u']

word = list(sys.stdin.readline().strip())
newWord = []
i = 0

while i < len(word):
    newWord.append(word[i])
    if word[i] in mo:
        i += 2

    i += 1

print(''.join(newWord))
