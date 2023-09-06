import sys

k = int(sys.stdin.readline())

tmp = k * 0.01 + 25

if tmp < 100:
    tmp = 100
elif tmp > 2000:
    tmp = 2000

print("{:.2f}".format(tmp))