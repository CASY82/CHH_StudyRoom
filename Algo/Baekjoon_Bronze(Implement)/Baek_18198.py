import sys

play = list(sys.stdin.readline().strip())

a = 0
b = 0
match_point = False

for i in range(0, len(play), 2):
    if play[i] == "A":
        a += int(play[i+1])
    else:
        b += int(play[i+1])

    if a == b == 10:
        match_point = True

    if not match_point:
        if a > b and a >= 11:
            print("A")
            break
        elif b > a and b >= 11:
            print("B")
            break
    else:
        if abs(a-b) >= 2:
            if a > b:
                print("A")
            else:
                print("B")
            break