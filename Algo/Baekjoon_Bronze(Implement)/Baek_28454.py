import sys
from datetime import datetime

now = datetime.strptime(sys.stdin.readline().strip(), "%Y-%m-%d")

n = int(sys.stdin.readline())
cnt = 0

for _ in range(n):
    ticket = datetime.strptime(sys.stdin.readline().strip(), "%Y-%m-%d")

    if ticket >= now:
        cnt += 1

print(cnt)