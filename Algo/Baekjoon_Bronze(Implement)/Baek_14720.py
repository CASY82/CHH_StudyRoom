import sys

n = int(sys.stdin.readline())

milk_store = list(map(int, sys.stdin.readline().split()))
now = 0
cnt = 0

for i in range(n):
    if milk_store[i] == now:
        now = (now+1) % 3
        cnt += 1

print(cnt)