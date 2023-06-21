import sys

word = sys.stdin.readline().strip()

check = word[0]
cnt = 0

for i in range(len(word)):
    if word[i] == check:
        cnt += 1
    else:
        break

print(cnt)