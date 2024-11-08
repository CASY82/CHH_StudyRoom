import sys

n = int(sys.stdin.readline())
cnt = 0
origin = sys.stdin.readline().strip()
write = sys.stdin.readline().strip()

for i in range(n):
    if origin[i] == write[i]:
        cnt += 1

print(cnt)