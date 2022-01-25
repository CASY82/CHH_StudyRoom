import sys

n = int(sys.stdin.readline())
score = []

for _ in range(n):
    name, kr, en, math = map(str, sys.stdin.readline().strip().split())
    kr = int(kr)
    en = int(en)
    math = int(math)
    score.append([name, kr, en, math])

score.sort(key= lambda x:(-x[1], x[2], -x[3], x[0]))

for i in range(n):
    print(score[i][0])