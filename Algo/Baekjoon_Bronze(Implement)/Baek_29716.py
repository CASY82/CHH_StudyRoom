import sys

j, n = map(int, sys.stdin.readline().split())
res = 0

for _ in range(n):
    sentence = sys.stdin.readline().strip()
    score = 0

    for i in range(len(sentence)):
        if 65 <= ord(sentence[i]) <= 90:
            score += 4
        elif 97 <= ord(sentence[i]) <= 122 or 48 <= ord(sentence[i]) <= 57:
            score += 2
        elif ord(sentence[i]) == 32:
            score += 1

    if score <= j:
        res += 1

print(res)