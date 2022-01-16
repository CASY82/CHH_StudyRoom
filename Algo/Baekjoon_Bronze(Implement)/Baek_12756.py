import sys

PlayerA = list(map(int, sys.stdin.readline().split()))
PlayerB = list(map(int, sys.stdin.readline().split()))

while True:
    PlayerA[1] -= PlayerB[0]
    PlayerB[1] -= PlayerA[0]

    if PlayerA[1] <= 0 and PlayerB[1] <= 0:
        print("DRAW")
        break
    if PlayerA[1] <= 0:
        print("PLAYER B")
        break
    if PlayerB[1] <= 0:
        print("PLAYER A")
        break