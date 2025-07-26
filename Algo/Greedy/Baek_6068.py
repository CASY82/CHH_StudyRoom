import sys

n = int(sys.stdin.readline())
works = []
now = 99999999999999

for _ in range(n):
    need_time, end_time = map(int, sys.stdin.readline().split())

    works.append([need_time, end_time])

works.sort(key=lambda x:-x[1])

for i in range(n):
    now = min(now, works[i][1])
    now -= works[i][0]

    if now < 0:
        now = -1
        break

print(now)