import sys
now = 0

for _ in range(10):
    t = int(sys.stdin.readline())

    if t == 1:
        now += 90
    elif t == 2:
        now += 180
    elif t == 3:
        now -= 90

tmp = now % 360

if tmp == 0:
    print("N")
elif tmp == 90:
    print("E")
elif tmp == 180:
    print("S")
else:
    print("W")