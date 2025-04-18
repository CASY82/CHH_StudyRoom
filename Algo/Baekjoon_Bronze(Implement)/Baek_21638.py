import sys

t1, v1 = map(int, sys.stdin.readline().split())
t2, v2 = map(int, sys.stdin.readline().split())

if t2 < 0 and v2 >= 10:
    print("A storm warning for tomorrow! Be careful and stay home if possible!")
else:
    if t2 < t1:
        print("MCHS warns! Low temperature is expected tomorrow.")
    elif v1 < v2:
        print("MCHS warns! Strong wind is expected tomorrow.")
    else:
        print("No message")