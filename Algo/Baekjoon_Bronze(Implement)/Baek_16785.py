import sys

a, b, c = map(int, sys.stdin.readline().split())
day = 0
remain = 0

while (day * a + remain) < c:
    day += 1
    if day % 7 == 0:
        remain += b

print(day)