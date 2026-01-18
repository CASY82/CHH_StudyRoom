# Babelfish
import sys

data = sys.stdin.buffer.read().splitlines()
word_list = dict()
i = 0

while i < len(data) and data[i]:
    en_word, dialect_word = data[i].decode().split()

    word_list[dialect_word] = en_word
    i += 1

while i < len(data) and not data[i]:
    i += 1

for j in range(i, len(data)):
    w = data[j].decode().strip()

    if w not in word_list:
        print("eh")
    else:
        print(word_list[w])