import sys

n, m = map(int, sys.stdin.readline().split())
num = list(map(int, sys.stdin.readline().split()))
multiple = set()

for i in range(m):
    cnt = 1
    while True:
        tmp = cnt * num[i]
        if tmp > n:
            break
        multiple.add(tmp)
        cnt += 1

print(sum(multiple))