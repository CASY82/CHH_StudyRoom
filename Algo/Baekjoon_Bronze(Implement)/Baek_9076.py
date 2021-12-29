import sys

t = int(sys.stdin.readline())

for _ in range(t):
    score = list(map(int, sys.stdin.readline().split()))

    score.sort()
    score.pop(0)
    score.pop(-1)

    if abs(score[0] - score[-1]) >= 4:
        print("KIN")
    else:
        print(sum(score))
