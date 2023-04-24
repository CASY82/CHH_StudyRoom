import sys

n = int(sys.stdin.readline())
word = []
tmp = set()
result = 0

for _ in range(n):
    word.append(sys.stdin.readline().strip())

for i in range(n):
    if word[i] not in tmp:
        result += 1
    for j in range(len(word[i])):
        new_word = word[i][j:] + word[i][:j]
        if new_word not in tmp:
            tmp.add(new_word)

print(result)