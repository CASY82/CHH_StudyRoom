import sys

while True:
    Cheryl = 0
    Tania = 0
    cards = list(sys.stdin.readline().strip().split())

    if cards[0] == "#":
        break

    for i in range(len(cards)):
        if cards[i] != '*':
            if cards[i] == 'A' or int(cards[i]) % 2 == 1:
                Cheryl += 1
            elif int(cards[i]) % 2 == 0:
                Tania += 1

    if Cheryl > Tania:
        print("Cheryl")
    elif Cheryl < Tania:
        print("Tania")
    else:
        print("Draw")