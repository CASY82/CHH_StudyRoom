import sys

word = sys.stdin.readline().strip()
change_array = list(sys.stdin.readline().strip().split())

result = ""

for i in range(len(word)):
    if word[i] in change_array:
        result += word[i].lower()
    else:
        result += word[i]

print(result)