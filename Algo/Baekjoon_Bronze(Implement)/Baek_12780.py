import sys

h = sys.stdin.readline().strip()
n = sys.stdin.readline().strip()

cnt = 0

for i in range(len(h)):
    if h[i] == n[0]:
        if h[i:i+len(n)] == n:
            cnt += 1

print(cnt)