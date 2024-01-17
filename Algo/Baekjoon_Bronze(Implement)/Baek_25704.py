import sys

n = int(sys.stdin.readline())
p = int(sys.stdin.readline())

tmp = [p]

if n >= 20:
    tmp.append(p * 0.75)

if n >= 15:
    tmp.append(p - 2000)

if n >= 10:
    tmp.append(p * 0.9)

if n >= 5:
    tmp.append(p - 500)

if int(min(tmp)) < 0:
    print(0)
else:
    print(int(min(tmp)))