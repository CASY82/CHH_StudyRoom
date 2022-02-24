import sys

score = list(map(int, sys.stdin.readline().split()))

print(56 * score[0] + 24 * score[1] + 14 * score[2] + 6 * score[3])