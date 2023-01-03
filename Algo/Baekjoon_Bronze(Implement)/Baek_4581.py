import sys

while True:
    vote = list(sys.stdin.readline().strip())

    if vote[0] == "#":
        break

    yes = 0
    no = 0
    white = 0

    for i in range(len(vote)):
        if "Y" == vote[i]:
            yes += 1
        elif "N" == vote[i]:
            no += 1
        elif "A" == vote[i]:
            white += 1

    if white >= len(vote)/2:
        print("need quorum")
    else:
        if yes > no:
            print("yes")
        elif yes == no:
            print("tie")
        else:
            print("no")