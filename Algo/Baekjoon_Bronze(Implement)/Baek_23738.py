import sys

word = sys.stdin.readline().strip()
res = ""

changer = {
    "B": "v",
    "E": "ye",
    "H": "n",
    "P": "r",
    "C": "s",
    "Y": "u",
    "X": "h"
}

for i in range(len(word)):
    if word[i] in changer:
        res += changer[word[i]]
    else:
        res += word[i].lower()

print(res)