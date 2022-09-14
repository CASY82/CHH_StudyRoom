import sys

while True:
    try:
        n, s = map(int, sys.stdin.readline().split())
    except:
        break

    print(s // (n + 1))