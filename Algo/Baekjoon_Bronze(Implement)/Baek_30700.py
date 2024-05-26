import sys

word = sys.stdin.readline().strip()

korea = ["K", "O", "R", "E", "A"]
index = 0

for i in range(len(word)):
    if word[i] == korea[index % 5]:
        index += 1

print(index)