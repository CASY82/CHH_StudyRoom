import sys

word = sys.stdin.readline().strip()

joi = 0
ioi = 0

for alpha in range(len(word)):
    if word[alpha] == "I":
        if word[alpha:alpha+3] == "IOI":
            ioi += 1

    if word[alpha] == "J":
        if word[alpha:alpha+3] == "JOI":
            joi += 1

print(joi)
print(ioi)