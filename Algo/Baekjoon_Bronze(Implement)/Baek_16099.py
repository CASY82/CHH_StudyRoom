import sys

t = int(sys.stdin.readline())

for _ in range(t):
    lt, wt, le, we = map(int, sys.stdin.readline().split())

    eurecom = le * we
    tele = lt * wt

    if eurecom > tele:
        print("Eurecom")
    elif eurecom < tele:
        print("TelecomParisTech")
    else:
        print("Tie")