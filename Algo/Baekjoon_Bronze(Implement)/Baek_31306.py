import sys

word = sys.stdin.readline().strip()
cnt = 0
y_cnt = 0

for i in range(len(word)):
    if word[i] in {"a", "e", "i", "o", "u"}:
        cnt += 1
    elif word[i] == "y":
        y_cnt += 1

print(cnt, cnt + y_cnt)