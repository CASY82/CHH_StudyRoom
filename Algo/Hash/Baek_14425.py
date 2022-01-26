import sys

n, m = map(int, sys.stdin.readline().split())
oriString = set()
cnt = 0

for _ in range(n):
    oriString.add(sys.stdin.readline().strip())

for _ in range(m):
    word = sys.stdin.readline().strip()

    if word in oriString:
        cnt += 1

print(cnt)