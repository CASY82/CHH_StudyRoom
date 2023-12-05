import sys

word = sys.stdin.readline().strip()

length = len(word)
result = True

for i in range(length // 2):
    if word[i] != word[length-1-i]:
        result = False

if result:
    print("true")
else:
    print("false")