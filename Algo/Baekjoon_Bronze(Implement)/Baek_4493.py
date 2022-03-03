import sys

t = int(input())

for _ in range(t):
    n = int(sys.stdin.readline())
    score = [0, 0]

    for _ in range(n):
        p1, p2 = sys.stdin.readline().strip().split()

        if p1 == p2:
            continue
        else:
            if p1 == 'P' and p2 == 'R':
                score[0] += 1
            elif p1 == 'P' and p2 == 'S':
                score[1] += 1
            elif p1 == 'S' and p2 == 'P':
                score[0] += 1
            elif p1 == 'S' and p2 == 'R':
                score[1] += 1
            elif p1 == 'R' and p2 == 'S':
                score[0] += 1
            elif p1 == 'R' and p2 == 'P':
                score[1] += 1

    if score[0] > score[1]:
        print('Player 1')
    elif score[0] < score[1]:
        print('Player 2')
    else:
        print('TIE')