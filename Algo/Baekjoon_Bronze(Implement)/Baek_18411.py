import sys

score = list(map(int, sys.stdin.readline().split()))

score.sort()

print(score[-1] + score[-2])