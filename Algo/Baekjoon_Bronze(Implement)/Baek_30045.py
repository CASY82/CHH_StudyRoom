import sys

n = int(sys.stdin.readline())
cnt = 0

for _ in range(n):
    word = sys.stdin.readline().strip()

    if "01" in word or "OI" in word:
        cnt += 1

print(cnt)