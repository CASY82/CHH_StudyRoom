import sys

n = int(sys.stdin.readline())
word_dict = {
    "H": 0,
    "I": 0,
    "A": 0,
    "R": 0,
    "C": 0
}

word = sys.stdin.readline().strip()

for i in range(len(word)):
    if word[i] in word_dict:
        word_dict[word[i]] += 1

print(min(word_dict.values()))