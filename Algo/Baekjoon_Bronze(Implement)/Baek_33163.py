import sys

n = int(sys.stdin.readline())
word = sys.stdin.readline().strip()
res = ""

for i in range(len(word)):
    if word[i] == "J":
        res += "O"
    elif word[i] == "O":
        res += "I"
    elif word[i] == "I":
        res += "J"

print(res)