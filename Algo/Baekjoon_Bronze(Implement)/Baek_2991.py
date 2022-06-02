import sys

a, b, c, d = map(int, sys.stdin.readline().split())
p, m, n = map(int, sys.stdin.readline().split())

A_dog_total = a + b
B_dog_total = c + d

for arrival_time in (p, m, n):
    cnt = 0

    if (arrival_time % A_dog_total) <= a:
        if (arrival_time % A_dog_total) != 0:
            cnt += 1

    if (arrival_time % B_dog_total) <= c:
        if (arrival_time % B_dog_total) != 0:
            cnt += 1

    print(cnt)