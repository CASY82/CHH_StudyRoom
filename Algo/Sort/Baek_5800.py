import sys

k = int(sys.stdin.readline())

for z in range(k):
    maxMath = 0
    minMath = 0
    gap = 0
    classMath = list(map(int, sys.stdin.readline().split()))

    score = classMath[1:]

    score.sort()
    maxMath = score[-1]
    minMath = score[0]

    for i in range(1, len(score)):
        if gap < score[i] - score[i-1]:
            gap = score[i] - score[i-1]

    print("Class", z+1)
    print("Max ", maxMath, ", Min ", minMath, ", Largest gap ", gap, sep='')