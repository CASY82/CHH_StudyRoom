import sys

t = int(sys.stdin.readline())
answer = list(map(int, sys.stdin.readline().split()))
cnt = 0


for i in answer:
    if t == i:
        cnt += 1

print(cnt)