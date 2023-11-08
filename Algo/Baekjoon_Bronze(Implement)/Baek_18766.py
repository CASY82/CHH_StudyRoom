import sys

t = int(sys.stdin.readline())

for _ in range(t):
    n = int(sys.stdin.readline())
    card = list(sys.stdin.readline().strip().split())
    dolphin = list(sys.stdin.readline().strip().split())

    card.sort()
    dolphin.sort()
    result = True

    for i in range(n):
        if card[i] != dolphin[i]:
            result = False

    if result:
        print("NOT CHEATER")
    else:
        print("CHEATER")