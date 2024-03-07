import sys

n, u, l = map(int, sys.stdin.readline().split())

if n >= 1000:
    if u >= 8000 or l >= 260:
        print("Very Good")
    else:
        print("Good")
else:
    print("Bad")