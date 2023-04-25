import sys

d, h, m = map(int, sys.stdin.readline().split())

daysToMin = (d-11) * 60 * 24
hoursToMin = (h-11) * 60
minToMin = (m - 11)

result = daysToMin + hoursToMin + minToMin

if daysToMin < 0 and hoursToMin < 0 and minToMin < 0 or result < 0:
    print(-1)
else:
    print(result)