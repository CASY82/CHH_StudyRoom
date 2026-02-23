# 알파벳 점수 계산기
import sys

word = sys.stdin.readline().strip()

res = 1
score = 1

for i in range(len(word) - 1):
    if ord(word[i]) < ord(word[i + 1]):
        score += 1
    else:
        score = 1

    res += score

print(res)