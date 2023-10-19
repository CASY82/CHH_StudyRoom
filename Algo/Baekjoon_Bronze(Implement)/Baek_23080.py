import sys

n = int(sys.stdin.readline())
word = sys.stdin.readline().strip()

new_word = ""

for i in range(0, len(word), n):
    new_word += word[i]

print(new_word)