import sys

n, m = map(int, sys.stdin.readline().split())
locate = []
move = []
now = 0
cnt = 0

for _ in range(n):
    locate.append(int(sys.stdin.readline()))

for _ in range(m):
    move.append(int(sys.stdin.readline()))


for i in move:
    cnt += 1
    now += i
    if now >= n:
        break
    now += locate[now]
    if now >= n:
        break

print(cnt)