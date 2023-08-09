import sys

n, s = map(int, sys.stdin.readline().split())

times = list(map(int, sys.stdin.readline().split()))
lager = 0

for time in times:
    if lager < time * s:
        lager = time * s

if lager % 1000 != 0:
    print(lager // 1000 + 1)
else:
    print(lager // 1000)