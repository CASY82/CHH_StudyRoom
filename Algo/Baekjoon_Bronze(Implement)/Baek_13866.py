import sys

level = list(map(int, sys.stdin.readline().split()))

level.sort()

print(abs((level[0] + level[3]) - (level[1] + level[2])))