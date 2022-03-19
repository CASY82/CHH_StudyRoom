import sys

word = []

for _ in range(5):
    word.append(list(sys.stdin.readline().strip()))

result = ''
for i in range(15):
    for j in range(5):
        try:
            result += word[j][i]
        except:
            continue
print(result)