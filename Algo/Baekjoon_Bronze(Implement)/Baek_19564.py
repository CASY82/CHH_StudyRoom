import sys

s = sys.stdin.readline().strip()
cnt = 0
tmp = "Nope"

for word in range(len(s)):
    if tmp == "Nope":
        tmp = s[word]
        cnt += 1
    else:
        if ord(tmp) >= ord(s[word]):
            cnt += 1
        tmp = s[word]

print(cnt)