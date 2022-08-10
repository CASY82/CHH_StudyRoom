import sys

a, b, c, m = map(int, sys.stdin.readline().split())

time = 0
tired = 0
work = 0

if a > m:
   print(0)
else:
    while time < 24:
        if tired + a <= m: #이 부분 실수!
            tired += a
            work += b
        else:
            if tired - c <= 0:
                tired = 0
            else:
                tired -= c

        time += 1

    print(work)