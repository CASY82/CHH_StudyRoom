import sys

n = int(sys.stdin.readline())
yesterday = list(sys.stdin.readline().strip())
today = list(sys.stdin.readline().strip())
cnt = 0

for i in range(n):
    if yesterday[i] == today[i] and today[i] == "C":
       cnt += 1

print(cnt)