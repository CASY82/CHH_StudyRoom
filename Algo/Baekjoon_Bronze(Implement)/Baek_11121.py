import sys

t = int(sys.stdin.readline())

for _ in range(t):
    tongsin, dochak = sys.stdin.readline().strip().split()

    if tongsin == dochak:
        print("OK")
    else:
        print("ERROR")