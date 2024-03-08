import sys

n = int(sys.stdin.readline())
word = sys.stdin.readline().strip()

cnt = 0

for i in range(n // 2):
    if word[i] != word[len(word) - 1 - i]:
        cnt += 1

print(cnt)