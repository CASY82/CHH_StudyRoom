import sys

cho = list(map(int, sys.stdin.readline().split()))
han = list(map(int, sys.stdin.readline().split()))
score = [13, 7, 5, 3, 3, 2]

cho_total = 0
han_total = 0

for i in range(len(score)):
    cho_total += cho[i] * score[i]
    han_total += han[i] * score[i]

han_total += 1.5

if cho_total > han_total:
    print("cocjr0208")
else:
    print("ekwoo")