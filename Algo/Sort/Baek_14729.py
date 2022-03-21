import sys

n = int(sys.stdin.readline())
score = []

for _ in range(n):
    score.append(float(sys.stdin.readline()))

score.sort()
for i in range(7):
    print("{:.3f}".format(score[i]))