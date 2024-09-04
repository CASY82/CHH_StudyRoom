import sys

try:
    fir, sec = map(int, sys.stdin.readline().split())

    print(fir - sec)
except:
    print("NaN")