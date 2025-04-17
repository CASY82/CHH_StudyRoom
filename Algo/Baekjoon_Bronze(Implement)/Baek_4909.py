import sys

while True:
    score = list(map(int, sys.stdin.readline().split()))

    if score == [0, 0, 0, 0, 0, 0]:
        break

    total = sum(score) - max(score) - min(score)
    total /= 4

    if total == int(total):
        print(int(total))
    else:
        print(total)